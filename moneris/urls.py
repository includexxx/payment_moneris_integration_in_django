from django.urls import path
from . import views

app_name = 'moneris'

urlpatterns = [
    path('', views.moneris_list, name='moneris_list'),
    path('<int:pk>/', views.moneris_detail, name='moneris_detail'),
    path('new/', views.moneris_create, name='moneris_create'),
    path('update/<int:pk>/', views.moneris_create, name='moneris_update'),
    path('delete/<int:pk>/', views.moneris_delete, name='moneris_delete'),
    path('payment/validate', views.moneris_payment_validate, name='moneris_payment_validate'),


]