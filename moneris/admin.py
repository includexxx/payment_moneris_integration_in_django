from django.contrib import admin

from .models import Moneris


@admin.register(Moneris)
class MonerisAdmin(admin.ModelAdmin):
    list_display = ('name', 'ps_store_id', 'hpp_key', 'environment')
    search_fields = ('name', 'ps_store_id', 'environment')
