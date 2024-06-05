from django.shortcuts import render
from inventory.models import Beer, MerchItem

def index(request):
    """ Render the home page. """
    limited_edition_beers = Beer.objects.filter(limited_edition=True)[:3]
    print(limited_edition_beers)
    context = {
        'limited_edition_beers': limited_edition_beers
    }
    return render(request, 'home/index.html', context)
