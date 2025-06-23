from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('product/', views.product_list, name='product_list'),
    path('product/<int:pk>', views.product_detail, name='product_detail'),
    path('create_product/', views.create_product, name='create_product'),
    path('products/<int:product_id>/edit/', views.edit_product, name='edit_product'),

]
