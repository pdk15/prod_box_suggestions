from rest_framework import serializers
from .models import Product, ShippingBox

class OrderItemSerializer(serializers.Serializer):
    product_name=serializers.CharField(max_length=100)
    quantity=serializers.IntegerField()
    

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class BoxSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShippingBox
        fields = "__all__"