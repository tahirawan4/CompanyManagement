# my_project/urls.py
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView  # new
from core import views

urlpatterns = [
    path('trucks/', views.TruckListView.as_view(), name='trucks'),
    path('truck/drivers/', views.TruckDriverListView.as_view(), name='truck-drivers'),
    path('suppliers/', views.SupplierListView.as_view(), name='suppliers'),
    path('buyers/', views.BuyerListView.as_view(), name='buyers'),

    path('truck/add/', views.TruckCreateView.as_view(), name='truck-add'),
    path('truck/driver/add/', views.TruckDriverCreateView.as_view(), name='truck-driver-add'),
    path('supplier/add/', views.SupplierCreateView.as_view(), name='supplier-add'),
    path('buyer/add', views.BuyerCreateView.as_view(), name='buyer-add'),
]
