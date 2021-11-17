from django.urls import path

from .views import add_to_cart, remove_from_cart, CartList, update_cart, CheckoutList

urlpatterns = [
    path("cart/<int:product_id>/", add_to_cart, name="add_to_cart"),
    path("cart/remover/<int:product_id>/", remove_from_cart, name="remove_from_cart"),
    path("cart/", CartList.as_view(), name="cart_list"),
    path("cart/update/<int:product_id>/", update_cart, name="update_cart"),
    # checkout
    path("checkout/", CheckoutList.as_view(), name="checkout"),
]
