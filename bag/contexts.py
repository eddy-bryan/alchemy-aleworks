from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from inventory.models import Beer, MerchItem

def bag_contents(request):
    bag_items = []
    total = 0
    product_count = 0
    bag = request.session.get('bag', {})

    for key, value in bag.items():
        prefix, item_id = key.split('_', 1)
        quantity = value['quantity']

        if prefix == 'beer':
            product = get_object_or_404(Beer, pk=item_id)
        elif prefix == 'merch':
            product = get_object_or_404(MerchItem, pk=item_id)

        total += quantity * product.price
        product_count += quantity
        bag_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'product': product,
            'type': prefix,
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
