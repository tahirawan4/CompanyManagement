from django.urls import path
from products import views

urlpatterns = [
    path('items/', views.ItemsListView.as_view(), name='items'),
    path('item/packaging/', views.ItemPackagingListView.as_view(), name='item-packaging'),
    path('item/add/', views.ItemCreateView.as_view(), name='item-add'),
    path('item/packaging/add/', views.ItemPackagingCreateView.as_view(), name='packaging-add'),
]
