from django.urls import path
from .views import ProductsListView, ProductDetailView, category_view

urlpatterns = [
    path("", ProductsListView.as_view(), name="products_list"),
    path("<str:slug>/", ProductDetailView.as_view(), name="product_detail"),
    path("category/<str:slug>/", category_view, name="category"),
]
