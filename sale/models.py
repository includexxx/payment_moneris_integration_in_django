from django.db import models

from moneris.models import Moneris


class SaleOrder(models.Model):
    status = (
        ('draft', 'Draft'),
        ('paid', 'Paid'),
        ('cancelled', 'Cancel')
    )
    sale_order = models.AutoField(primary_key=True)
    payment = models.CharField(choices=status,default='draft', null=False, blank=False, max_length=111)
    payment_acquire = models.ForeignKey(Moneris, related_name='payment_by', on_delete=models.SET_NULL,null=True)
    price = models.FloatField(null=False, blank=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

