from django.shortcuts import (
    render,
    redirect,
    reverse,
    get_object_or_404,
    HttpResponse
)
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from .models import Order, BeerLineItem, MerchLineItem
from inventory.models import Beer, MerchItem
from profiles.forms import CustomerProfileForm
from profiles.models import CustomerProfile
from bag.contexts import bag_contents

import stripe
import json


@require_POST
def cache_checkout_data(request):
    """
    View to cache checkout data for Stripe PaymentIntent.

    Caches bag contents and user info in Stripe PaymentIntent metadata.
    """
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'bag': json.dumps(request.session.get('bag', {})),
            'save_info': request.POST.get('save_info'),
            'username': request.user,
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(
            request,
            "Payment processing failed. Please try again later."
        )
        return HttpResponse(content=e, status=400)


def checkout(request):
    """
    Checkout view to handle POST requests for placing orders.

    Handles form submission for creating orders and processing payments.
    """
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        bag = request.session.get('bag', {})

        form_data = {
            'customer_name': request.POST['customer_name'],
            'customer_email': request.POST['customer_email'],
            'customer_phone': request.POST['customer_phone'],
            'customer_country': request.POST['customer_country'],
            'customer_postcode': request.POST['customer_postcode'],
            'customer_city': request.POST['customer_city'],
            'customer_address1': request.POST['customer_address1'],
            'customer_address2': request.POST['customer_address2'],
            'customer_county': request.POST['customer_county'],
        }
        order_form = OrderForm(form_data)
        if order_form.is_valid():
            order = order_form.save(commit=False)
            pid = request.POST.get('client_secret').split('_secret')[0]
            order.stripe_pid = pid
            order.original_bag = json.dumps(bag)
            order.save()
            for key, item_data in bag.items():
                item_type, item_id = key.split('_')
                try:
                    if item_type == 'beer':
                        product = Beer.objects.get(id=item_id)
                        if 'items_by_size' in item_data:
                            for size, quantity in (
                                item_data['items_by_size'].items()
                            ):
                                beer_line_item = BeerLineItem(
                                    order=order,
                                    beer=product,
                                    quantity=quantity,
                                )
                                beer_line_item.save()
                        else:
                            beer_line_item = BeerLineItem(
                                order=order,
                                beer=product,
                                quantity=item_data['quantity'],
                            )
                            beer_line_item.save()
                    elif item_type == 'merch':
                        product = MerchItem.objects.get(id=item_id)
                        if 'items_by_size' in item_data:
                            for size, quantity in (
                                item_data['items_by_size'].items()
                            ):
                                merch_line_item = MerchLineItem(
                                    order=order,
                                    merch_item=product,
                                    quantity=quantity,
                                    merch_item_size=size,
                                )
                                merch_line_item.save()
                        else:
                            merch_line_item = MerchLineItem(
                                order=order,
                                merch_item=product,
                                quantity=item_data['quantity'],
                            )
                            merch_line_item.save()
                except (Beer.DoesNotExist, MerchItem.DoesNotExist):
                    messages.error(
                        request,
                        "Product not found. Please contact us for assistance."
                    )
                    order.delete()
                    return redirect(reverse('view_bag'))

            request.session['save_info'] = 'save-info' in request.POST
            return redirect(
                reverse(
                    'checkout_success',
                    args=[order.order_number]
                )
            )
        else:
            messages.error(
                request,
                'Error in form. Verify info and try again.'
            )
    else:
        bag = request.session.get('bag', {})
        if not bag:
            messages.error(request, "Your bag is empty!")
            # Redirect back to the current page
            return redirect(request.META.get('HTTP_REFERER', reverse('home')))

        current_bag = bag_contents(request)
        total = current_bag['grand_total']
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

        # Attempt to prefill the form with user's profile info
        if request.user.is_authenticated:
            try:
                profile = CustomerProfile.objects.get(customer=request.user)
                order_form = OrderForm(initial={
                    'customer_name': profile.customer.get_full_name(),
                    'customer_email': profile.customer.email,
                    'customer_phone': profile.default_customer_phone,
                    'customer_country': profile.default_customer_country,
                    'customer_postcode': profile.default_customer_postcode,
                    'customer_city': profile.default_customer_city,
                    'customer_address1': profile.default_customer_address1,
                    'customer_address2': profile.default_customer_address2,
                    'customer_county': profile.default_customer_county,
                })
            except CustomerProfile.DoesNotExist:
                order_form = OrderForm()
        else:
            order_form = OrderForm()

    if not stripe_public_key:
        message.warning(
            request,
            'Stripe public key is missing. Ensure it is correctly set.'
        )

    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)


def checkout_success(request, order_number):
    """
    View for displaying checkout success page.

    Displays order details and sends confirmation email to customer.
    """
    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)

    if request.user.is_authenticated:
        profile = CustomerProfile.objects.get(customer=request.user)
        # Attach the user's profile to the order
        order.customer_profile = profile
        order.save()

        # Save the user's info
        if save_info:
            profile_data = {
                'default_customer_phone': order.customer_phone,
                'default_customer_country': order.customer_country,
                'default_customer_postcode': order.customer_postcode,
                'default_customer_city': order.customer_city,
                'default_customer_address1': order.customer_address1,
                'default_customer_address2': order.customer_address2,
                'default_customer_county': order.customer_county,
            }
            customer_profile_form = CustomerProfileForm(
                profile_data,
                instance=profile
            )
            if customer_profile_form.is_valid():
                customer_profile_form.save()

    messages.success(
        request,
        f'Your order has been successfully processed! '
        f'Your order number is {order_number}. '
        f'A confirmation email will be sent to {order.customer_email}.'
    )

    if 'bag' in request.session:
        del request.session['bag']

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
    }

    return render(request, template, context)
