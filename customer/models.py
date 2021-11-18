from django.db import models
from django.contrib.auth import get_user_model

from products.models import Product


class Cart(models.Model):
    products = models.ManyToManyField(Product, related_name="cart")
    user = models.ForeignKey(
        get_user_model(), related_name="cart_items", on_delete=models.CASCADE
    )

    def __str__(self):
        return self.user.username


class Order(models.Model):
    PAYMENT_METHODS = (
        ("Mpamba", "Mpamba"),
        ("Airtel Money", "Airtel Money"),
        ("National bank", "National Bank"),
        ("Kaku Pay", "Kaku Pay"),
    )

    user = models.ManyToManyField(get_user_model(), related_name="orders")
    products = models.ManyToManyField(Product, related_name="orders")
    address = models.CharField(max_length=255)
    description = models.TextField()
    payment_method = models.CharField(max_length=255, choices=PAYMENT_METHODS)
    reference = models.CharField(max_length=255)

    def __str__(self):
        return self.user.name
