from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    """
    View to display the checkout page.
    """
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('colas'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51P3GMn07huOrQK6Os13paIuoZxHiGtzy6Xukl0jP8g23LmVwJx3obnfESz1pyAR4IQP5gS7vcElMz48LFkQWfBTG00RBfUuITI',
        'client_secret': 'test_client_secret',
    }

    return render(request, template, context)
