# my_project/urls.py
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView  # new
from invoices import views

urlpatterns = [
    path('invoices/', views.InvoiceListView.as_view(), name='invoices'),

    path('invoice/add/', views.InvoiceCreateView.as_view(), name='invoice-add'),
    ]
