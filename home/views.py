from django.shortcuts import render
from inventory.models import Beer, MerchItem

def index(request):
    """ Render the home page. """
    limited_edition_beers = Beer.objects.filter(limited_edition=True)[:3]
    random_merch_items = MerchItem.get_random_merch_items(quantity=3)
    context = {
        'limited_edition_beers': limited_edition_beers,
        'random_merch_items': random_merch_items,
    }
    return render(request, 'home/index.html', context)
