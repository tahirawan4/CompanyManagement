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

    path('truck/<int:pk>/update/', views.TruckUpdateView.as_view(), name='truck-update'),
    path('truck/driver/<int:pk>/update/', views.TruckDriverUpdateView.as_view(), name='truck-driver-update'),
    path('supplier/<int:pk>/update/', views.SupplierUpdateView.as_view(), name='supplier-update'),
    path('buyer/<int:pk>/update/', views.BuyerUpdateView.as_view(), name='buyer-update'),

    path('truck/<int:pk>/delete/', views.TruckDeleteView.as_view(), name='truck-delete'),
    path('truck/driver/<int:pk>/delete/', views.TruckDriverDeleteView.as_view(), name='truck-driver-delete'),
    path('supplier/<int:pk>/delete/', views.SupplierDeleteView.as_view(), name='supplier-delete'),
    path('buyer/<int:pk>/delete/', views.BuyerDeleteView.as_view(), name='buyer-delete'),

]
