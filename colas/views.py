from django.shortcuts import render
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