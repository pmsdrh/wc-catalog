from django.urls import path

from .views import update_product, update_products

urlpatterns = [
    path('update-product/', update_product),
    path('multi/update-products/', update_products)
]
