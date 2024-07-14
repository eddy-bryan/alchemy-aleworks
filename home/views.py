from django.shortcuts import render

from inventory.models import Beer, MerchItem

def index(request):
    """
    Render the home page with limited edition beers and random merchandise items.

    Retrieves a list of limited edition beers and random merchandise items
    from the database and renders them on the home page.

    Parameters:
    - request: HttpRequest object representing the request from the client.

    Returns:
    - HttpResponse object rendering the 'home/index.html' template with context data.
    """
    limited_edition_beers = Beer.get_random_beers(limited_edition=True, quantity=3)
    random_merch_items = MerchItem.get_random_merch_items(quantity=3)
    context = {
        'limited_edition_beers': limited_edition_beers,
        'random_merch_items': random_merch_items,
    }
    return render(request, 'home/index.html', context)
