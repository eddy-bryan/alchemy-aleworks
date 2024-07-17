from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404

from inventory.models import Beer, MerchItem


def bag_contents(request):
    """
    Calculate and return the contents of the shopping bag.

    This function retrieves the items in the shopping bag from the session,
    calculates the total cost, the number of products, and determines the
    delivery cost based on the total value of the bag contents.

    Returns a context dictionary containing:
    - bag_items: List of items in the bag with their details.
    - total: Total cost of the items in the bag.
    - product_count: Total number of items in the bag.
    - delivery: Delivery cost based on the total value.
    - free_delivery_delta: Amount needed to qualify for free delivery.
    - free_delivery_threshold: Threshold value for free delivery.
    - grand_total: Total cost including delivery.
    """
    bag_items = []
    total = 0
    product_count = 0
    bag = request.session.get('bag', {})

    for item_id, item_data in bag.items():
        prefix, raw_item_id = item_id.split('_', 1)
        if prefix == 'beer':
            item_type = 'beer'
            product = get_object_or_404(Beer, pk=raw_item_id)
        elif prefix == 'merch':
            item_type = 'merch'
            product = get_object_or_404(MerchItem, pk=raw_item_id)

        if 'items_by_size' in item_data:
            for size, quantity in item_data['items_by_size'].items():
                total += quantity * product.price
                product_count += quantity
                bag_items.append({
                    'item_id': item_id,
                    'item_type': item_type,
                    'quantity': quantity,
                    'product': product,
                    'size': size,
                })
        else:
            quantity = item_data['quantity']
            total += quantity * product.price
            product_count += quantity
            bag_items.append({
                'item_id': item_id,
                'item_type': item_type,
                'quantity': quantity,
                'product': product,
            })

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = Decimal(settings.STANDARD_DELIVERY)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = Decimal(0)
        free_delivery_delta = Decimal(0)

    grand_total = total + delivery

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }

    return context
