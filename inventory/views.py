from django.shortcuts import render
from .models import Beer

def beers(request):
    """ A view to show, filter and sort all beers. """
    beers = Beer.objects.all()
    context = {
        'beers': beers,
    }
    return render(request, 'inventory/beers.html', context)
