from django.contrib import admin
from .models import NewsletterSignup


class NewsletterAdmin(admin.ModelAdmin):
    list_display = (
        'newsletter_email',
        'newsletter_first_name',
    )


admin.site.register(NewsletterSignup, NewsletterAdmin)
