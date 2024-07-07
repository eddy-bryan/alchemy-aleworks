from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from .models import Order, BeerLineItem, MerchLineItem
from inventory.models import Beer, MerchItem
from bag.contexts import bag_contents

import stripe
import json

@require_POST
def cache_checkout_data(request):
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
        messages.error(request, "We're unable to process your payment at the moment. Please try again later.")
        return HttpResponse(content=e, status=400)

def checkout(request):
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
                            for size, quantity in item_data['items_by_size'].items():
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
                            for size, quantity in item_data['items_by_size'].items():
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
                    messages.error(request, (
                        "One of the products in your cart could not be found in our database. Please contact us for assistance.")
                    )
                    order.delete()
                    return redirect(reverse('view_bag'))

            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse('checkout_success', args=[order.order_number]))
        else:
            messages.error(request, 'There seems to be an error in your form. Please verify your information and try again.')
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

        order_form = OrderForm()

    if not stripe_public_key:
        message.warning(request, 'Stripe public key is missing. Ensure it is correctly set in your environment.')

    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)


def checkout_success(request, order_number):
    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)
    messages.success(request, f'Your order has been successfully processed! Your order number is {order_number}. A confirmation email will be sent to {order.customer_email}.')

    if 'bag' in request.session:
        del request.session['bag']

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
    }

    return render(request, template, context)
