from django.contrib import admin
from django.urls import path

from app.views import index_page, product_detail_page, add_product, add_comment

urlpatterns = [
    path('', index_page, name='index'),
    path('category/<int:category_id>', index_page, name='category_by_id'),
    path('detail/<int:product_id>', product_detail_page, name='product-detail'),
    path('add-product/', add_product, name='add_product'),
    path('detail/<int:product_id>/comment', add_comment, name='add_comment'),
]