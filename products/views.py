from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.core.exceptions import ObjectDoesNotExist

from .models import Product, Category


class ProductsListView(ListView):
    model = Product
    template_name = "products/products_list.html"
    context_object_name = "products"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cart_products"] = self.request.user.cart_items.all()
        return context


class ProductDetailView(DetailView):
    model = Product
    template_name = "products/product_detail.html"
    context_object_name = "product"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cart_products"] = self.request.user.cart_items.all()
        context["related_products"] = Product.objects.filter(
            category__in=self.object.category.all()
        )[:11]
        return context


def category_view(request, slug):
    try:
        category = Category.objects.get(slug=slug)
        products = Product.objects.filter(category=category)
    except ObjectDoesNotExist:
        products = []

    # cart
    cart_products = request.user.cart_items.all()
    return render(
        request,
        "products/products_list.html",
        {"products": products, "cart_products": cart_products},
    )
