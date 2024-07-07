from django.http import HttpResponse

from .models import Order, BeerLineItem, MerchLineItem
from inventory.models import Beer, MerchItem

import json
import time


class StripeWH_Handler:
    """Handles Stripe webhook events"""

    def __init__(self, request):
        """
        Initialize with the incoming HTTP request.

        Args:
            request (HttpRequest): The HTTP request object containing the webhook data.
        """
        self.request = request

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
            return HttpResponse(
                content=f'Webhook received: {event["type"]} | SUCCESS: Verified order already in database',
                status=200)
        else:
            order = None
            try:
                order = Order.objects.create(
                    customer_name=shipping_details.name,
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
