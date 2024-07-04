from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from inventory.models import Beer, MerchItem

def bag_contents(request):
    bag_items = []
    total = 0
    product_count = 0
    bag = request.session.get('bag', {})

    for item_id, item_data in bag.items():
        prefix, raw_item_id = item_id.split('_', 1)
        if prefix == 'beer':
            product = get_object_or_404(Beer, pk=raw_item_id)
        elif prefix == 'merch':
            product = get_object_or_404(MerchItem, pk=raw_item_id)

        if 'items_by_size' in item_data:
            for size, quantity in item_data['items_by_size'].items():
                item_total = quantity * product.price
                total += item_total
                product_count += quantity
                bag_items.append({
                    'item_id': item_id,
                    'quantity': quantity,
                    'product': product,
                    'size': size,
                    'item_total': item_total,
                })
        else:
            quantity = item_data['quantity']
            item_total = quantity * product.price
            total += item_total
            product_count += quantity
            bag_items.append({
                'item_id': item_id,
                'quantity': quantity,
                'product': product,
                'item_total': item_total,
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
