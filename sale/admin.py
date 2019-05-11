from django.contrib import admin

# Register your models here.
from .models import SaleOrder

admin.site.register(SaleOrder)
