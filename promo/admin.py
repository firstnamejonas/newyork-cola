from django.contrib import admin
from .models import Contest


class ContestAdmin(admin.ModelAdmin):
    list_display = ('contest_username', 'contest_ordernumber')


admin.site.register(Contest, ContestAdmin)
