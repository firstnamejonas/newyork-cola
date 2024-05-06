from django.contrib import admin
from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = (
        'contact_email',
        'contact_ordernumber',
        'contact_issue',
    )


admin.site.register(Contact, ContactAdmin)
