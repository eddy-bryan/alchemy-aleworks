from django.conf import settings
from django.shortcuts import render
from inventory.models import Beer


def taproom(request):
    """
    Render the Taproom page.

    Retrieves the Google Maps API key from settings and passes it to the
    template context.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: Rendered response with the Taproom page.
    """
    template = 'pages/taproom.html'
    context = {
        'GOOGLE_MAPS_API_KEY': settings.GOOGLE_MAPS_API_KEY,
    }

    return render(request, template, context)


def about(request):
    """
    Render the About page.

    Retrieves a list of random beers and passes them to the template context.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: Rendered response with the About page.
    """
    random_beers = Beer.get_random_beers(quantity=3)
    context = {
        'random_beers': random_beers,
    }
    return render(request, 'pages/about.html', context)


def orders_and_returns(request):
    """
    Render the Orders and Returns page.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: Rendered response with the Orders and Returns page.
    """
    return render(request, 'pages/orders_and_returns.html')


def privacy_policy(request):
    """
    Render the Privacy Policy page.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: Rendered response with the Privacy Policy page.
    """
    return render(request, 'pages/privacy_policy.html')


def terms_and_conditions(request):
    """
    Render the Terms and Conditions page.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: Rendered response with the Terms and Conditions page.
    """
    return render(request, 'pages/terms_and_conditions.html')
