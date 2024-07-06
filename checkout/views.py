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
    }

    return render(request, template, context)
