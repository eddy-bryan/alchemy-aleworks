from django.http import HttpResponse
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings

from .models import Order, BeerLineItem, MerchLineItem
from inventory.models import Beer, MerchItem
from profiles.models import CustomerProfile

import json
import time
import stripe


class StripeWH_Handler:
    """
    Handles Stripe webhook events, adapted for this project from the Boutique Ado walkthrough.
    """

    def __init__(self, request):
        """
        Initialize with the incoming HTTP request.

        Args:
            request (HttpRequest): The HTTP request object containing the webhook data.
        """
        self.request = request

    def _send_confirmation_email(self, order):
        """
        Send a confirmation email to the customer after completing an order.

        Args:
            order (Order): The Order object for which to send the confirmation email.
        """
        customer_email = order.customer_email
        subject = render_to_string(
            'checkout/confirmation_emails/confirmation_email_subject.txt',
            {'order': order})
        body = render_to_string(
            'checkout/confirmation_emails/confirmation_email_body.txt',
            {'order': order, 'contact_email': settings.DEFAULT_FROM_EMAIL})
            
        send_mail(
            subject,
            body,
            settings.DEFAULT_FROM_EMAIL,
            [customer_email]
        )

    def handle_event(self, event):
        """
        Handle any unrecognized or unexpected webhook event from Stripe.

        Args:
            event (dict): The event payload received from Stripe.

        Returns:
            HttpResponse: A response indicating the event was received but not handled specifically.
        """
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200
        )

    def handle_payment_intent_succeeded(self, event):
        """
        Handle the `payment_intent.succeeded` event from Stripe.

        Args:
            event (dict): The event payload received from Stripe, indicating a successful payment.

        Returns:
            HttpResponse: A response confirming receipt of the successful payment intent.
        """
        intent = event.data.object
        pid = intent.id
        bag = intent.metadata.bag
        save_info = intent.metadata.save_info

        # Get the Charge object
        stripe_charge = stripe.Charge.retrieve(
            intent.latest_charge
        )

        billing_details = stripe_charge.billing_details
        shipping_details = intent.shipping
        grand_total = round(stripe_charge.amount / 100, 2)

        # Clean data in the shipping details
        for field, value in shipping_details.address.items():
            if value == "":
                shipping_details.address[field] = None

        # Update profile information if save_info was checked
        profile = None
        username = intent.metadata.username
        if username != 'AnonymousUser':
            profile = CustomerProfile.objects.get(customer__username=username)
            if save_info:
                profile.default_customer_phone = shipping_details.phone
                profile.default_customer_country = shipping_details.address.country
                profile.default_customer_postcode = shipping_details.address.postal_code
                profile.default_customer_city = shipping_details.address.city
                profile.default_customer_address1 = shipping_details.address.line1
                profile.default_customer_address2 = shipping_details.address.line2
                profile.default_customer_county = shipping_details.address.state
                profile.save()

        order_exists = False
        attempt = 1
        while attempt <= 5:
            try:
                order = Order.objects.get(
                    customer_name__iexact=shipping_details.name,
                    customer_email__iexact=billing_details.email,
                    customer_phone__iexact=shipping_details.phone,
                    customer_country__iexact=shipping_details.address.country,
                    customer_postcode__iexact=shipping_details.address.postal_code,
                    customer_city__iexact=shipping_details.address.city,
                    customer_address1__iexact=shipping_details.address.line1,
                    customer_address2__iexact=shipping_details.address.line2,
                    customer_county__iexact=shipping_details.address.state,
                    grand_total=grand_total,
                    original_bag=bag,
                    stripe_pid=pid,
                )
                order_exists = True
                break
            except Order.DoesNotExist:
                attempt += 1
                time.sleep(1)
        if order_exists:
            self._send_confirmation_email(order)
            return HttpResponse(
                content=f'Webhook received: {event["type"]} | SUCCESS: Verified order already in database',
                status=200)
        else:
            order = None
            try:
                order = Order.objects.create(
                    customer_name=shipping_details.name,
                    customer_profile=profile,
                    customer_email=billing_details.email,
                    customer_phone=shipping_details.phone,
                    customer_country=shipping_details.address.country,
                    customer_postcode=shipping_details.address.postal_code,
                    customer_city=shipping_details.address.city,
                    customer_address1=shipping_details.address.line1,
                    customer_address2=shipping_details.address.line2,
                    customer_county=shipping_details.address.state,
                    original_bag=bag,
                    stripe_pid=pid,
                )
                for item_id, item_data in json.loads(bag).items():
                    item_type, item_id = key.split('_')
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
            except Exception as e:
                if order:
                    order.delete()
                return HttpResponse(
                    content=f'Webhook received: {event["type"]} | ERROR: {e}',
                    status=500)
        self._send_confirmation_email(order)
        return HttpResponse(
            content=f'Webhook received: {event["type"]} | SUCCESS: Created order in webhook',
            status=200)

    def handle_payment_intent_payment_failed(self, event):
        """
        Handle the `payment_intent.payment_failed` event from Stripe.

        Args:
            event (dict): The event payload received from Stripe, indicating a failed payment.

        Returns:
            HttpResponse: A response confirming receipt of the failed payment intent.
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200
        )
