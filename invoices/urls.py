# my_project/urls.py
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView  # new
from invoices import views

urlpatterns = [
    path('invoices/', views.InvoiceListView.as_view(), name='invoices'),
    path('invoice/add/', views.InvoiceCreateView.as_view(), name='invoice-add'),
    path('invoice/<int:pk>/delete/', views.InvoiceDeleteView.as_view(), name='invoice-delete'),
    path('invoice/<int:pk>/update/', views.InvoiceUpdateView.as_view(), name='invoice-update'),


    path('years/', views.YearListView.as_view(), name='years'),
    path('year/add/', views.YearCreateView.as_view(), name='year-add'),
    path('year/<int:pk>/delete/', views.YearDeleteView.as_view(), name='year-delete'),
    path('year/<int:pk>/update/', views.YearUpdateView.as_view(), name='year-update'),
]
