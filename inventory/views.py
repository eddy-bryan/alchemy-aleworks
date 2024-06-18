from django.shortcuts import render, get_object_or_404
from .models import Beer, MerchItem

def beers(request):
    """ A view to show, filter and sort all beers. """
    beers = Beer.objects.all()
    limited_edition_beer = Beer.get_random_beers(limited_edition=True, quantity=1)
    core_range_beer = Beer.get_random_beers(limited_edition=False, quantity=1)
    context = {
        'beers': beers,
        'limited_edition_beer': limited_edition_beer[0] if limited_edition_beer else None,
        'core_range_beer': core_range_beer[0] if core_range_beer else None,
    }
    return render(request, 'inventory/beers.html', context)

def merch(request):
    """ A view to show a detailed page for an individual beer. """
    merch = MerchItem.objects.all()
    random_apparel = MerchItem.get_random_merch_items(category="Apparel & Accessories", quantity=1)
    random_drinkware = MerchItem.get_random_merch_items(category="Drinkware", quantity=1)
    context = {
        'merch': merch,
        'random_apparel': random_apparel[0] if random_apparel else None,
        'random_drinkware': random_drinkware[0] if random_drinkware else None,
    }
    return render(request, 'inventory/merch.html', context)

def beer_detail(request, beer_id):
    """ A view to show, filter and sort all beers. """
    beer = get_object_or_404(Beer, pk=beer_id)
    random_beers = Beer.get_random_beers(quantity=3, exclude_id=beer_id)
    context = {
        'beer': beer,
        'random_beers': random_beers,
    }
    return render(request, 'inventory/beer_detail.html', context)
