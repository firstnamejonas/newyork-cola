from django.shortcuts import render


def view_bag(request):
    """
    This view renders the shopping bag contents page.
    """

    return render(request, 'bag/bag.html')