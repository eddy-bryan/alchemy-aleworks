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

def add_to_bag(request, item_id):
    """Adds a number of items to the bag depending on the selected quantity"""

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list (bag.keys()):
        bag[item_id] += quantity
    else:
        bag[item_id] = quantity

    request.session['bag'] = bag
    print(request.session['bag'])
    return redirect(redirect_url)
