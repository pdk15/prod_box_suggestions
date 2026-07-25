from django.contrib import admin
from .models import Product, ShippingBox, Order

admin.site.register(Product)
admin.site.register(ShippingBox)
admin.site.register(Order)