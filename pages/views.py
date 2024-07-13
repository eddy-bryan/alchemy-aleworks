from django.conf import settings
from django.shortcuts import render
from inventory.models import Beer

def taproom(request):
    """ Render the Taproom page. """
    template = 'pages/taproom.html'
    context = {
        'GOOGLE_MAPS_API_KEY': settings.GOOGLE_MAPS_API_KEY,
    }

    return render(request, template, context)

def about(request):
    """ Render the About page. """
    random_beers = Beer.get_random_beers(quantity=3)
    context = {
        'random_beers': random_beers,
    }
    return render(request, 'pages/about.html', context)

def orders_and_returns(request):
    """ Render the orders and returns policy page. """
    return render(request, 'pages/orders_and_returns.html')

def privacy_policy(request):
    """ Render the privacy policy page. """
    return render(request, 'pages/privacy_policy.html')

def terms_and_conditions(request):
    """ Render the terms and conditions page. """
    return render(request, 'pages/terms_and_conditions.html')
