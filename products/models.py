from io import BytesIO
from PIL import Image

from django.core.files import File
from django.db import models
from django.utils import timezone
from django.urls import reverse

from users.models import CustomUser as User


class Color(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Size(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Supplier(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class ShippingCost(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name + " - " + str(self.price)


class ProductImage(models.Model):
    image = models.ImageField()
    thumbnail = models.ImageField(null=True, blank=True)

    def get_image(self):
        if self.image:
            return "http://127.0.01:8000/static" + self.image.url
        else:
            return ""

    def get_thumbnail(self):
        if self.thumbnail:
            return "http://127.0.0.1:8000/static" + self.thumbnail.url
        else:
            if self.image:
                self.thumbnail = self.create_thumbnail(self.image)
                self.save()
                return "http://127.0.0.1:8000/static" + self.thumbnail.url
            else:
                return ""

    def save(self, *args, **kwargs):
        self.thumbnail = self.create_thumbnail(self.image)
        super(ProductImage, self).save(*args, **kwargs)

    def create_thumbnail(self, image, size=(300, 300)):
        img = Image.open(image)
        img.convert("RGB")
        img.thumbnail(size)

        thumb_io = BytesIO()
        img.save(thumb_io, "JPEG", quality=95)

        thumbnail = File(thumb_io, name=image.name)

        return thumbnail

    def __str__(self):
        return str(self.image.url)


class Category(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="images")
    isFetured = models.BooleanField(default=False)
    slug = models.SlugField(null=True, blank=True)
    parent_category = models.ManyToManyField("self", blank=True)

    class meta:
        ordering = ["name"]

    def get_image(self):
        if self.image:
            return "http://127.0.0.1:8000/static" + self.image.url

        else:
            return ""

    def save(self, *args, **kwargs):
        self.slug = str(self.name).replace(" ", "-")
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    colors = models.ForeignKey(Color, related_name="product", on_delete=models.CASCADE)
    sizes = models.ForeignKey(Size, related_name="product", on_delete=models.CASCADE)
    ordered_from = models.CharField(max_length=50)
    suppliers = models.ManyToManyField(Supplier, related_name="product")
    shipping_price = models.ForeignKey(
        ShippingCost, related_name="product", on_delete=models.CASCADE
    )
    images = models.ManyToManyField(ProductImage, related_name="product")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    slug = models.SlugField()
    category = models.ManyToManyField(
        Category,
        related_name="products",
    )
    tags = models.ForeignKey(Tag, related_name="products", on_delete=models.CASCADE)
    isFeatured = models.BooleanField(default=False)
    is_onsale = models.BooleanField(default=False)
    is_top_rated = models.BooleanField(default=True)
    is_best_seller = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    added_by = models.OneToOneField(
        User, related_name="products_added", on_delete=models.CASCADE
    )
    description = models.CharField(max_length=255)

    class Meta:
        ordering = ["-created"]

    def __str__(self):
        return self.name + " " + str(self.price)

    def get_price(self):
        if self.price:
            return float(self.price) + (float(self.price) * 0.12)

    def save(self, *args, **kwargs):
        self.slug = str(self.name).replace(" ", "-")
        super(Product, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("product_detail", kwargs={"slug": self.slug})
