from django.urls import path

from .views import (
    store_order_create,
    store_order_update,
    store_order_update_from_warehouse,
    store_order_delete,
    store_order_detail
)

urlpatterns = [
    path('create/', store_order_create, name="store-order-create"),
    path('update/<str:pk>/', store_order_update, name="store-order-update"),
    path('update-from-warehouse/<str:pk>/', store_order_update_from_warehouse, name="store-order-update-from-warehouse"),
    path('delete/<str:pk>/', store_order_delete, name="store-order-delete"),
    path('detail/<str:pk>/', store_order_detail, name="store-order-detail"),
]