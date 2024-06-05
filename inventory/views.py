from django.shortcuts import render
from .models import Beer, MerchItem

def beers(request):
    """ A view to show, filter and sort all beers. """
    beers = Beer.objects.all()
    context = {
        'beers': beers,
    }
    return render(request, 'inventory/beers.html', context)

def merch(request):
    """ A view to show, filter and sort all beers. """
    merch = MerchItem.objects.all()
    context = {
        'merch': merch,
    }
    return render(request, 'inventory/merch.html', context)
