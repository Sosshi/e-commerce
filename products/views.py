from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Product, Category


class ProductsListView(LoginRequiredMixin, ListView):
    model = Product
    template_name = "products/products_list.html"
    context_object_name = "products"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cart_products"] = self.request.user.cart_items.first().products.all()
        return context


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    template_name = "products/product_detail.html"
    context_object_name = "product"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cart_products"] = self.request.user.cart_items.first().products.all()
        context["related_products"] = Product.objects.filter(
            category__in=self.object.category.all()
        )[:11]
        return context


@login_required
def category_view(request, slug):
    try:
        category = Category.objects.get(slug=slug)
        products = Product.objects.filter(category=category)
    except ObjectDoesNotExist:
        products = []

    # cart
    cart_products = request.user.cart_items.first().products.all()
    return render(
        request,
        "products/products_list.html",
        {"products": products, "cart_products": cart_products},
    )
