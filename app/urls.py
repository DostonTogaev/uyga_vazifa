from django.contrib import admin
from django.urls import path

from app.views import index_page, product_detail_page, add_product, add_comment, add_order, edit_product, delete_product
from app.auth import login_page, logout_page, register_page

urlpatterns = [
    path('', index_page, name='index'),
    path('category/<int:category_id>', index_page, name='category_by_id'),
    path('detail/<int:product_id>', product_detail_page, name='product-detail'),
    path('add-product/', add_product, name='add_product'),
    path('detail/<int:product_id>/comment', add_comment, name='add_comment'),
    path('detail/<int:product_id>/order', add_order, name='add_order'),
    path('detail/<int:pk>/delete-product', delete_product, name='delete'),
    path('detail/<int:pk>/edit-product', edit_product, name='edit'),

    path('login-page/', login_page, name='login'),
    path('logout/', logout_page, name='logout'),
    path('register/', register_page, name='register'),

]
