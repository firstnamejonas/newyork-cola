from django.shortcuts import render, get_object_or_404
from .models import Cola


def all_colas(request):
    """
    View to show all New York Cola Products
    (It's a one product store, so it's not necessary right now
    but for future maintainability and more projects it's better.)
    """

    colas = Cola.objects.all()

    context = {
        'colas': colas,
    }

    return render(request, 'colas/all_colas.html', context)


def product_page(request, cola_id):
    """
    View to display product page of a cola.
    """

    cola = get_object_or_404(Cola, pk=cola_id)

    context = {
        'cola': cola,
    }

    return render(request, 'colas/product_page.html', context)