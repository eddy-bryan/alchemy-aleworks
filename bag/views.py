from django.shortcuts import render, redirect
from inventory.models import Beer, MerchItem

def view_bag(request):
    """ Render the contents of the shopping bag. """
    random_beer = Beer.get_random_beers(quantity=1)
    random_merch = MerchItem.get_random_merch_items(quantity=1)
    context = {
        'random_beer': random_beer[0] if random_beer else None,
        'random_merch': random_merch[0] if random_merch else None,
    }
    return render(request, 'bag/bag.html', context)

def add_to_bag(request, item_id, item_type):
    """Adds a number of items to the bag depending on the selected quantity"""

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    size = request.POST.get('product_size', None)  # Correctly get size from POST
    bag = request.session.get('bag', {})

    key = f"{item_type}_{item_id}"

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
    else:
        if key in bag:
            bag[key]['quantity'] += quantity
        else:
            bag[key] = {'quantity': quantity}

    request.session['bag'] = bag
    return redirect(redirect_url)
