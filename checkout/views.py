from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from .forms import OrderForm

def checkout(request):
    bag = request.session.get('bag', {})
    order_form = OrderForm()

    if not bag:
        messages.error(request, "Your bag is empty!")
        # Redirect back to the current page
        return redirect(request.META.get('HTTP_REFERER', reverse('home')))

    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51PCo78GXMyHurIcyTXXzaYZ5takOVfX5YWqbfgN2X65Mma76BGrQVzMBYL54aTBHbHoui4b90bK3LpHcoEEe8HMC00wpkrVt9O',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
