from django.contrib import admin
from .models import (
    Color,
    Tag,
    Product,
    ProductImage,
    ShippingCost,
    Size,
    Category,
    Supplier,
)

admin.site.register(Color)
admin.site.register(Tag)
admin.site.register(Product)
admin.site.register(ProductImage)
admin.site.register(ShippingCost)
admin.site.register(Size)
admin.site.register(Category)
admin.site.register(Supplier)
