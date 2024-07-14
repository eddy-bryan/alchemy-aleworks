from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import CustomerProfile
from .forms import CustomerProfileForm

from checkout.models import Order


@login_required
def profile(request):
    """
    Display the user's profile.

    Retrieves the CustomerProfile instance associated with the logged-in user.
    If the request method is POST, updates the profile information based on form data.
    Displays a success message upon successful profile update.

    Template: 'profiles/profile.html'
    Context:
        - form: CustomerProfileForm instance for editing profile details.
        - orders: QuerySet of Order objects associated with the user's profile.
    """
    profile = get_object_or_404(CustomerProfile, customer=request.user)

    if request.method == 'POST':
        form = CustomerProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully.')

    form = CustomerProfileForm(instance=profile)
    orders = profile.orders.all()

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
    }

    return render(request, template, context)

def order_history(request, order_number):
    """
    Display details of a past order.

    Retrieves the Order instance based on the order_number provided.
    Displays an info message indicating that the page shows past order details.
    Renders the 'checkout/checkout_success.html' template with order details.

    Args:
        - order_number: Order number of the past order to display.

    Template: 'checkout/checkout_success.html'
    Context:
        - order: Order instance corresponding to the provided order_number.
        - from_profile: Boolean indicating if the order detail view was accessed from the user's profile.
    """
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)
