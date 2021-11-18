from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from django.contrib.auth import get_user_model


from products.models import Category, Product


class HomePage(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["featured_categories"] = Category.objects.filter(isFetured=True)
        context["featured_products"] = Product.objects.filter(isFeatured=True)
        context["products_on_sale"] = Product.objects.filter(is_onsale=True)
        context["top_rated_products"] = Product.objects.filter(is_top_rated=True)
        context["best_saler_products"] = Product.objects.filter(is_best_seller=True)
        context["categories"] = Category.objects.all()
        if self.request.user.is_authenticated:
            context[
                "cart_products"
            ] = self.request.user.cart_items.first().products.all()

        return context


class ContactPage(TemplateView):
    template_name = "contact.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cart_products"] = self.request.user.cart_items.first().products.all()
        return context


class SignUpView(CreateView):
    template_name = "registration/signup.html"
    model = get_user_model()
    fields = ["username", "email", "password"]
    success_url = "/accounts/login/"
