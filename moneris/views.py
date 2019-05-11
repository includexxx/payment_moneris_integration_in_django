from django.shortcuts import render,get_object_or_404, redirect

from .models import Moneris
from .forms import MonerisForm
from sale.models import SaleOrder
import requests
import pdb
from django.views.decorators.csrf import csrf_exempt

def moneris_list(request):
    object_list = Moneris.objects.all()
    return render(request, 'moneris/moneris_list.html', {'object_list': object_list})


def moneris_detail(request, pk):
    object = get_object_or_404(Moneris, pk=pk)
    return render(request, 'moneris/moneris_detail.html', {'object': object})


def moneris_create(request, **kwargs):
    pk = kwargs.get('pk')
    if pk:
        object = get_object_or_404(Moneris, pk=pk)
        form = MonerisForm(instance=object, data=request.POST or None)
    else:
        form = MonerisForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect("moneris:moneris_list")
    return render(request, 'moneris/moneris_create.html', {'form': form})


def moneris_delete(request, pk):
    object = get_object_or_404(Moneris, pk=pk)
    object.delete()
    return redirect('moneris:moneris_list')

@csrf_exempt
def moneris_payment_validate(request):
    kwargs = request.POST
    if request.method == 'POST':
        order_id = kwargs.get('response_order_id')
        sale_order_obj = SaleOrder.objects.get(sale_order=int(order_id))
        if sale_order_obj:
            url = sale_order_obj.payment_acquire._get_moneris_urls(sale_order_obj.status)['moneris_auth_url']
            info = {
                'ps_store_id': sale_order_obj.payment_acquire.ps_store_id,
                'hpp_key': sale_order_obj.payment_acquire.hpp_key,
                'charge_total': sale_order_obj.price,
                'order_id': sale_order_obj.sale_order,
                'validate_url': url
            }
            new_post = dict(ps_store_id=info['ps_store_id'], hpp_key=info['hpp_key'], transactionKey=kwargs.get('transactionKey'))
            r = requests.post(url=info['validate_url'], data=new_post)
            resp = r.text


            part = resp.split('<br>')
            new_response = dict([s.split(' = ') for s in part])

            success = kwargs.get('response_code')

            try:
                if (int(success) < 50 and kwargs.get('result') == '1' and
                        new_response.get('response_code') is not 'null' and int(new_response.get('response_code')) < 50 and
                        new_response.get('status') == 'Valid-Approved' and
                        new_response.get('amount') is not 'null' and float(new_response.get('amount')) == float(
                            kwargs.get('charge_total')) and
                        new_response.get('transactionKey') == kwargs.get('transactionKey') and
                        new_response.get('order_id') == kwargs.get('response_order_id')
                ):

                    sale_order_obj.payment = 'paid'
                    sale_order_obj.payment = 'cancelled'
            except ValueError:
                sale_order_obj.payment = 'cancelled'
            #pdb.set_trace()
            sale_order_obj.save()

        return redirect("sale:sale_order_list")

