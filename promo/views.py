from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContestForm
from .models import Contest
from checkout.models import Order


def contest_page(request):
    """
    View to display contest page and to
    check if form is valid.
    """
    if request.method == 'POST':
        form = ContestForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['contest_username']
            ordernumber = form.cleaned_data['contest_ordernumber']
            # Check whether the user name and order number exist in database.
            if Order.objects.filter(
                user_profile__user__username=username,
                order_number=ordernumber
            ).exists():
                # Check if the order number is already in the contest database.
                if Contest.objects.filter(
                    contest_ordernumber=ordernumber
                ).exists():
                    messages.error(
                        request,
                        "Oops! You've already entered the contest with this order number!"  # noqa
                    )
                else:
                    form.save()
                    messages.success(request, 'Your entry has been submitted successfully!')  # noqa
                    return redirect('contest_page')
            else:
                messages.error(request, 'Invalid username or order number.')
    else:
        form = ContestForm()
    return render(request, 'promo/contest_page.html', {'form': form})
