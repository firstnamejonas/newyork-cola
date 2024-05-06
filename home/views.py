from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import NewsletterForm
from .models import NewsletterSignup


def index(request):
    """
    View to return the index page + handle form functionality.
    """
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            newsletter_first_name = form.cleaned_data['newsletter_first_name']
            newsletter_email = form.cleaned_data['newsletter_email']
            form.save()
            messages.success(
                request,
                """THANK YOU!
                You've signed up successfully to our newsletter!"""
            )
            return redirect('home')
        else:
            messages.error(request, 'Oops! somethin went wrong there!')
    else:
        form = NewsletterForm()
    return render(request, 'home/index.html', {'form': form})
