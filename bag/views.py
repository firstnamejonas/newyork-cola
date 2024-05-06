from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404  # noqa
from django.contrib import messages
from colas.models import Cola


def view_bag(request):
    """
    This view renders the shopping bag contents page.
    """

    return render(request, 'bag/bag.html')


def add_items(request, item_id):
    """
    View to add New York Cola products to the shopping bag.
    """

    product = get_object_or_404(Cola, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
        messages.success(
            request,
            f'{product.product_name} successfully updated in your bag!'
        )
    else:
        bag[item_id] = quantity
        messages.success(
            request,
            f'{product.product_name} successfully added to your shopping bag!'
        )

    request.session['bag'] = bag
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """
    View to adjust the shopping bag.
    """

    product = get_object_or_404(Cola, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})

    if quantity > 0:
        bag[item_id] = quantity
        messages.success(
            request,
            f'{product.product_name} quantity has been updated!'
        )
    else:
        bag.pop(item_id)
        messages.success(
            request,
            f'{product.product_name} removed from your bag!'
        )

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def delete_items(request, item_id):
    """
    View to delete items from the shopping bag.
    """
    product = get_object_or_404(Cola, pk=item_id)
    try:
        bag = request.session.get('bag', {})
        messages.success(
            request,
            f'{product.product_name} removed from your bag!'
        )
        bag.pop(item_id)

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)
