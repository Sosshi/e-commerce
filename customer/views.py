from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.views.generic import ListView, CreateView

from products.models import Product

from .models import Cart, Order


# cart views
@login_required
def add_to_cart(request, product_id):
    if Cart.objects.filter(user=request.user).count():
        product = Product.objects.filter(pk=product_id).first()
        request.user.cart_items.first().products.add(product)
    else:
        cart = Cart.objects.create(user=request.user)
        cart.products.add(Product.objects.filter(pk=product_id).first())

    cart_products = request.user.cart_items.first().products.all()

    return render(
        request, "customers/componets/cart.html", {"cart_products": cart_products}
    )


@login_required
def remove_from_cart(request, product_id):
    product = request.user.cart_items.first().products.get(pk=product_id)
    request.user.cart_items.first().products.remove(product)
    cart_products = request.user.cart_items.first().products.all()

    return render(
        request, "customers/componets/cart.html", {"cart_products": cart_products}
    )


@login_required
def update_cart(request, product_id):
    quantity = request.POST.get("qty")
    if quantity:
        cart = Cart.objects.get(pk=product_id)
        cart.quantity = int(quantity)
        cart.save()
    cart_products = request.user.cart_items.first().products.all()
    return render(
        request, "customers/componets/cart_list.html", {"cart_products": cart_products}
    )


class CartList(LoginRequiredMixin, ListView):
    model = Cart
    context_object_name = "cart_items"
    template_name = "customers/cart.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cart_products"] = self.request.user.cart_items.first().products.all()
        return context


class CheckoutList(LoginRequiredMixin, CreateView):
    model = Order
    template_name = "customers/checkout.html"
    fields = ["address", "description", "payment_method", "reference"]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cart_products"] = self.request.user.cart_items.first().products.all()
        return context
