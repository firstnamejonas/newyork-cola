from django.shortcuts import render, get_object_or_404
from .models import UserProfile

def profile(request):
    """
    View to display userprofile template.
    """
    profile = get_object_or_404(UserProfile, user=request.user)

    template = 'userprofiles/userprofile.html'
    context = {
        'profile': profile,
    }

    return render(request, template, context)
