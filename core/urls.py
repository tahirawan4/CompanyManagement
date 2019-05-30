# my_project/urls.py
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView  # new
from core import views

urlpatterns = [
    path('trucks/', views.TruckListView.as_view(), name='trucks'),
    path('truck/drivers/', views.TruckDriverListView.as_view(), name='trucks'),
    path('suppliers/', views.SupplierListView.as_view(), name='trucks'),
    path('buyers/', views.BuyerListView.as_view(), name='trucks'),
]
