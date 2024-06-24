from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.contrib import messages
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

def search_view(request):
    query = request.GET.get('q', '').strip()  # Get the search query

    if not query:
        messages.error(request, "Please enter a search term to find products.")
        return redirect(request.META.get('HTTP_REFERER', 'home'))  # Redirect to the referring page or 'home' if no referrer.

    # Construct queries to filter beers and merch items based on the search term
    beer_queries = Q(name__icontains=query) | Q(sku__icontains=query) | Q(type__icontains=query) | Q(description__icontains=query) | Q(alcohol_content__icontains=query)
    merch_queries = Q(name__icontains=query) | Q(sku__icontains=query) | Q(category__icontains=query) | Q(description__icontains=query)

    # Query the database
    beers = Beer.objects.filter(beer_queries)
    merch_items = MerchItem.objects.filter(merch_queries)

    context = {
        'query': query,
        'beers': beers,
        'merch_items': merch_items,
    }

    return render(request, 'inventory/search_results.html', context)

def beer_detail(request, beer_id):
    """ A detailed view to show a specific beer. """
    beer = get_object_or_404(Beer, pk=beer_id)
    random_beers = Beer.get_random_beers(quantity=3, exclude_id=beer_id)
    context = {
        'beer': beer,
        'random_beers': random_beers,
    }
    return render(request, 'inventory/beer_detail.html', context)

def merch_detail(request, merch_id):
    """ A detailed view to show a specific merch item. """
    merch = get_object_or_404(MerchItem, pk=merch_id)
    random_merch = MerchItem.get_random_merch_items(quantity=3, exclude_id=merch_id)
    context = {
        'merch': merch,
        'random_merch': random_merch,
    }
    return render(request, 'inventory/merch_detail.html', context)
