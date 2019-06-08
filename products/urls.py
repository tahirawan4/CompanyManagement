from django.urls import path
from products import views

urlpatterns = [
    path('items/', views.ItemsListView.as_view(), name='items'),
    path('item/packaging/', views.ItemPackagingListView.as_view(), name='item-packaging'),
    path('item/add/', views.ItemCreateView.as_view(), name='item-add'),
    path('item/<int:pk>/update/', views.ItemUpdateView.as_view(), name='item-update'),
    path('item/<int:pk>/delete/', views.ItemDeleteView.as_view(), name='item-delete'),
    path('item/packaging/add/', views.ItemPackagingCreateView.as_view(), name='packaging-add'),
    path('item/packaging/<int:pk>/update/', views.ItemPackagingUpdateView.as_view(), name='packaging-update'),
    path('item/packaging/<int:pk>/delete/', views.ItemPackagingDeleteView.as_view(), name='packaging-delete'),
]
