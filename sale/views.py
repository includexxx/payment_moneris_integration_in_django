from django.shortcuts import render, redirect
import requests
# Create your views here.
from .models import SaleOrder
from .forms import SaleOrderForm

import pdb


def sale_order_list(request):
    sol = SaleOrder.objects.all()
    return render(request, 'sale/sale_order_list.html', {'object_list':sol})


def sale_order_create(request):
    form = SaleOrderForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            soo = form.save()
            if soo.sale_order:
                url = soo.payment_acquire._get_moneris_urls(soo.status)['moneris_form_url']
                form = {
                   'ps_store_id': soo.payment_acquire.ps_store_id,
                   'hpp_key': soo.payment_acquire.hpp_key,
                   'charge_total': soo.price,
                   'order_id': soo.sale_order,
                    'url': url
               }
                return render(request, 'sale/payment.html', {'form': form})

    return render(request, 'sale/sale_order_create.html', {'form':form})

