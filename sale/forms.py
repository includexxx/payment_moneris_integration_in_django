from django import forms

from .models import SaleOrder


class SaleOrderForm(forms.ModelForm):
    class Meta:
        model = SaleOrder
        fields = ('payment_acquire', 'price')