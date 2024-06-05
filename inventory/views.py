from django.shortcuts import render
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
    """ A view to show, filter and sort all beers. """
    merch = MerchItem.objects.all()
    context = {
        'merch': merch,
    }
    return render(request, 'inventory/merch.html', context)
