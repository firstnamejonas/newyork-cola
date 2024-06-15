from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404  # noqa
from django.contrib import messages
from .models import Cola
from .forms import ProductForm


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


def add_cola(request):
    """
    Add a cola to the store as a superuser
    """

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added a new cola!')
            return redirect(reverse('add_cola'))
        else:
            messages.error(
                request,
                'Failed to add product. Please ensure the form is valid.'
            )
    else:
        form = ProductForm()

    form = ProductForm()
    template = 'colas/add_cola.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


def edit_cola(request, cola_id):
    """
    Edit a product in the store.
    """
    product = get_object_or_404(Cola, pk=cola_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                f'Successfully updated {product.product_name}!'
            )
            return redirect(reverse('product_page', args=[product.id]))
        else:
            messages.error(
                request,
                'Failed to update product. Please ensure the form is valid.'
            )
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are now editing {product.product_name}!')

    template = 'colas/edit_cola.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)
