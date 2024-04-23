

def bag_contents(request):
    """
    Context processor function.
    """

    bag_items = []
    total = 0
    product_count = 0

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
    }

    return context
