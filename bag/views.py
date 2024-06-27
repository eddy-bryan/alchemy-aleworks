from django.shortcuts import render
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
