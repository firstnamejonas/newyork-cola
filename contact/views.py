from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm
from .models import Contact


def contact_page(request):
    """
    View to display contact page and to
    check if form is valid.
    """
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact_full_name = form.cleaned_data['contact_full_name']
            contact_email = form.cleaned_data['contact_email']
            contact_ordernumber = form.cleaned_data['contact_ordernumber']
            contact_issue = form.cleaned_data['contact_issue']
            contact_message = form.cleaned_data['contact_message']
            form.save()
            messages.success(
                request,
                """Your Message has been send successfully! 
                We will answer you a quickly as possible!"""
            )
            return redirect('contact_page')
        else:
            messages.error(request, 'Invalid username or order number.')
    else:
        form = ContactForm()
    return render(request, 'contact/contact_page.html', {'form': form})
