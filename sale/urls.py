from django.urls import path

from . import views
app_name = 'sale'

urlpatterns = [
    path('', views.sale_order_list, name='sale_order_list'),
    path('new/', views.sale_order_create, name='sale_order_create'),

]