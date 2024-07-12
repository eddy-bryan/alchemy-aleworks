from django.shortcuts import render
from inventory.models import Beer

def taproom(request):
    """ Render the Taproom page. """
    return render(request, 'pages/taproom.html')

def about(request):
    """ Render the About page. """
    random_beers = Beer.get_random_beers(quantity=3)
    context = {
        'random_beers': random_beers,
    }
    return render(request, 'pages/about.html', context)

def privacy_policy(request):
    """ Render the privacy policy page. """
    return render(request, 'pages/privacy_policy.html')
