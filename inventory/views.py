from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.db.models import Q
from django.contrib import messages

from .models import Beer, MerchItem
from .forms import BeerForm, MerchItemForm

def beers(request):
    """ A view to show, filter and sort all beers. """
    limited_edition = request.GET.get('limited_edition', '').lower() == 'true'
    beers = Beer.objects.all()

    # Filter based on limited edition
    if limited_edition:
        beers = beers.filter(limited_edition=True)
        title = "Limited Edition Beers"
    elif request.GET.get('limited_edition', '').lower() == 'false':
        beers = beers.filter(limited_edition=False)
        title = "Core Range Beers"
    else:
        title = "All Beers"

    # Sorting functionality
    sort_by = request.GET.get('sort_by')
    if sort_by == 'price_asc':
        beers = beers.order_by('price')
    elif sort_by == 'price_desc':
        beers = beers.order_by('-price')
    elif sort_by == 'name_asc':
        beers = beers.order_by('name')
    elif sort_by == 'name_desc':
        beers = beers.order_by('-name')
    elif sort_by == 'alcohol_asc':
        beers = beers.order_by('alcohol_content')
    elif sort_by == 'alcohol_desc':
        beers = beers.order_by('-alcohol_content')

    # Get random beers
    limited_edition_beer = Beer.get_random_beers(limited_edition=True, quantity=1)
    core_range_beer = Beer.get_random_beers(limited_edition=False, quantity=1)
    context = {
        'beers': beers,
        'limited_edition_beer': limited_edition_beer[0] if limited_edition_beer else None,
        'core_range_beer': core_range_beer[0] if core_range_beer else None,
        'title': title,
        'limited_edition': request.GET.get('limited_edition', ''),
    }
    return render(request, 'inventory/beers.html', context)

def merch(request):
    """ A view to show, filter and sort all merch items. """
    category = request.GET.get('category', '').lower()
    merch = MerchItem.objects.all()

    # Filter based on category
    if category == 'drinkware':
        merch = merch.filter(category__iexact='Drinkware')
        title = "Drinkware"
    elif category == 'apparel & accessories':
        merch = merch.filter(category__iexact='Apparel & Accessories')
        title = "Apparel & Accessories"
    else:
        title = "All Merch"

    # Sorting functionality
    sort_by = request.GET.get('sort_by')
    if sort_by == 'price_asc':
        merch = merch.order_by('price')
    elif sort_by == 'price_desc':
        merch = merch.order_by('-price')
    elif sort_by == 'name_asc':
        merch = merch.order_by('name')
    elif sort_by == 'name_desc':
        merch = merch.order_by('-name')

    # Get random merch items
    random_apparel = MerchItem.get_random_merch_items(category="Apparel & Accessories", quantity=1)
    random_drinkware = MerchItem.get_random_merch_items(category="Drinkware", quantity=1)
    context = {
        'merch': merch,
        'random_apparel': random_apparel[0] if random_apparel else None,
        'random_drinkware': random_drinkware[0] if random_drinkware else None,
        'title': title,
        'category': request.GET.get('category', ''),
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

def add_beer(request):
    """
    A view for admins to be able to add beers to the store without needing to use the admin interface.
    """
    if request.method == 'POST':
        form = BeerForm(request.POST, request.FILES)
        if form.is_valid():
            beer = form.save()
            messages.success(request, 'Beer successfully added!')
            return redirect(reverse('beer_detail', args=[beer.id]))
        else:
            messages.error(request, 'Failed to add beer. Please ensure the form is valid.')
    else:
        form = BeerForm()
        
    form = BeerForm()
    template = 'inventory/add_beer.html'
    context = {
        'form': form,
    }

    return render(request, template, context)

def add_merch(request):
    """
    A view for admins to be able to add merch items to the store without needing to use the admin interface.
    """
    if request.method == 'POST':
        form = MerchItemForm(request.POST, request.FILES)
        if form.is_valid():
            merch = form.save()
            messages.success(request, 'Merch item successfully added!')
            return redirect(reverse('merch_detail', args=[merch.id]))
        else:
            messages.error(request, 'Failed to add merch item. Please ensure the form is valid.')
    else:
        form = MerchItemForm()

    form = MerchItemForm()
    template = 'inventory/add_merch.html'
    context = {
        'form': form,
    }

    return render(request, template, context)

def edit_beer(request, beer_id):
    """
    A view for admins to be able to edit beers in the store without needing to use the admin interface.
    """
    beer = get_object_or_404(Beer, pk=beer_id)
    if request.method == 'POST':
        form = BeerForm(request.POST, request.FILES, instance=beer)
        if form.is_valid():
            form.save()
            messages.success(request, 'Beer successfully updated!')
            return redirect(reverse('beer_detail', args=[beer.id]))
        else:
            messages.error(request, 'Failed to update beer. Please ensure the form is valid.')
    else:
        form = BeerForm(instance=beer)
        messages.info(request, f'You are editing {beer.name}')

    template = 'inventory/edit_beer.html'
    context = {
        'form': form,
        'beer': beer,
    }

    return render(request, template, context)

def edit_merch(request, merch_id):
    """
    A view for admins to be able to edit merch items in the store without needing to use the admin interface.
    """
    merch = get_object_or_404(MerchItem, pk=merch_id)
    if request.method == 'POST':
        form = MerchItemForm(request.POST, request.FILES, instance=merch)
        if form.is_valid():
            form.save()
            messages.success(request, 'Merch item successfully updated!')
            return redirect(reverse('merch_detail', args=[merch.id]))
        else:
            messages.error(request, 'Failed to update merch item. Please ensure the form is valid.')
    else:
        form = MerchItemForm(instance=merch)
        messages.info(request, f'You are editing {merch.name}')

    form = MerchItemForm(instance=merch)
    messages.info(request, f'You are editing {merch.name}')

    template = 'inventory/edit_merch.html'
    context = {
        'form': form,
        'merch': merch,
    }

    return render(request, template, context)

def delete_beer(request, beer_id):
    """
    A view for admins to be able to delete beers from the store without needing to use the admin interface.
    """
    beer = get_object_or_404(Beer, pk=beer_id)
    beer.delete()
    messages.success(request, 'Beer deleted successfully!')
    return redirect(reverse('beers'))

def delete_merch(request, merch_id):
    """
    A view for admins to be able to delete merch items from the store without needing to use the admin interface.
    """
    merch = get_object_or_404(MerchItem, pk=merch_id)
    merch.delete()
    messages.success(request, 'Merch item deleted successfully!')
    return redirect(reverse('merch'))
