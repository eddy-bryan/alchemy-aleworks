from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.exceptions import ValidationError

from inventory.models import Beer, MerchItem


def view_bag(request):
    """
    Render the contents of the shopping bag.
    """
    random_beer = Beer.get_random_beers(quantity=1)
    random_merch = MerchItem.get_random_merch_items(quantity=1)
    context = {
        'random_beer': random_beer[0] if random_beer else None,
        'random_merch': random_merch[0] if random_merch else None,
    }
    return render(request, 'bag/bag.html', context)


def add_to_bag(request, item_id, item_type):
    """
    Adds a specified quantity of a beer or merchandise item to the bag.

    If the item has a size, it is added to the bag with size-specific
    quantities. If no size is specified, the item is added with a general
    quantity.

    Parameters:
    - item_id: ID of the item to add (Beer or MerchItem)
    - item_type: Type of the item ('beer' or 'merch')

    Redirects back to the URL specified in the POST request.
    """
    product = get_object_or_404(
        Beer if item_type == 'beer' else MerchItem,
        pk=item_id
    )

    redirect_url = request.POST.get('redirect_url')
    size = request.POST.get('product_size', None)
    bag = request.session.get('bag', {})
    key = f"{item_type}_{item_id}"

    try:
        quantity = int(request.POST.get('quantity'))
        if quantity <= 0:
            raise ValidationError("Quantity must be greater than zero.")

        if size:
            if key in bag:
                if 'items_by_size' not in bag[key]:
                    bag[key]['items_by_size'] = {}
                if size in bag[key]['items_by_size']:
                    bag[key]['items_by_size'][size] += quantity
                else:
                    bag[key]['items_by_size'][size] = quantity
            else:
                bag[key] = {'items_by_size': {size: quantity}}
            messages.success(
                request,
                f'{quantity} x {product.name} ({size.upper()}) added to bag.'
            )
        else:
            if key in bag:
                bag[key]['quantity'] += quantity
            else:
                bag[key] = {'quantity': quantity}
            messages.success(
                request,
                f'{quantity} x {product.name} added to bag.'
            )

    except ValueError:
        messages.error(
            request,
            "Invalid quantity. Please enter a valid number."
        )
    except ValidationError as e:
        messages.error(request, e.message)

    request.session['bag'] = bag
    return redirect(redirect_url)


def update_bag(request, item_type, item_id):
    """
    Update the quantity of a specified item in the bag.

    If the item has a size, the quantity for the specific size is updated.
    If no size is specified, the general quantity of the item is updated.

    Parameters:
    - item_type: Type of the item ('beer' or 'merch')
    - item_id: ID of the item to update (Beer or MerchItem)

    Redirects back to the bag view.
    """
    product = get_object_or_404(
        Beer if item_type == 'beer' else MerchItem,
        pk=item_id
    )

    try:
        quantity = int(request.POST.get('quantity'))

        size = request.POST.get('size', None)
        bag = request.session.get('bag', {})
        key = f"{item_type}_{item_id}"

        if size:
            if key in bag and 'items_by_size' in bag[key]:
                if quantity > 0:
                    bag[key]['items_by_size'][size] = quantity
                    messages.success(
                        request,
                        (f'{quantity} x {product.name} ({size.upper()}) '
                         'updated in your bag.')
                    )
                else:
                    del bag[key]['items_by_size'][size]
                    if not bag[key]['items_by_size']:
                        del bag[key]
                        messages.success(
                            request,
                            (f'{product.name} ({size.upper()}) '
                             'removed from your bag.')
                        )
            else:
                messages.warning(
                    request,
                    f'The item you are trying to update is not in your bag.'
                )
        else:
            if key in bag:
                if quantity > 0:
                    bag[key]['quantity'] = quantity
                    messages.success(
                        request,
                        f'{quantity} x {product.name} updated in your bag.'
                    )
                else:
                    del bag[key]
                    messages.success(
                        request,
                        f'{product.name} removed from your bag.'
                    )
            else:
                messages.warning(
                    request,
                    f'The item you are trying to update is not in your bag.'
                )

    except ValueError:
        messages.error(
            request,
            "Invalid quantity. Please enter a valid number."
        )
        return redirect('view_bag')
    except ValidationError as e:
        messages.error(request, e.message)
        return redirect('view_bag')

    request.session['bag'] = bag
    return redirect('view_bag')
