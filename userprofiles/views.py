from django.shortcuts import render


def profile(request):
    """
    View to display userprofile template.
    """

    template = 'userprofiles/userprofile.html'
    context = {}

    return render(request, template, context)
