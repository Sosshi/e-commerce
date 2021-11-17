from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, CreateView

from products.models import Product

from .models import Cart, Order


# cart views
def add_to_cart(request, product_id):
    cart = Cart.objects.create(quantity=1)
    product = Product.objects.get(pk=product_id)

    # add product to cart
    product.cart.add(cart)
    request.user.cart_items.add(cart)

    cart_products = request.user.cart_items.all()

    return render(
        request, "customers/componets/cart.html", {"cart_products": cart_products}
    )


def remove_from_cart(request, product_id):
    Cart.objects.filter(pk=product_id).delete()

    cart_products = request.user.cart_items.all()

    return render(
        request, "customers/componets/cart.html", {"cart_products": cart_products}
    )


def update_cart(request, product_id):
    quantity = request.POST.get("qty")
    if quantity:
        cart = Cart.objects.get(pk=product_id)
        cart.quantity = int(quantity)
        cart.save()
    cart_products = request.user.cart_items.all()
    return render(
        request, "customers/componets/cart_list.html", {"cart_products": cart_products}
    )


class CartList(ListView):
    model = Cart
    context_object_name = "cart_items"
    template_name = "customers/cart.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cart_products"] = self.request.user.cart_items.all()
        return context


class CheckoutList(CreateView):
    model = Order
    template_name = "customers/checkout.html"
    fields = ["address", "description", "payment_method", "reference"]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cart_products"] = self.request.user.cart_items.all()
        return context
