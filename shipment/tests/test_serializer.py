from django.test import TestCase
from shipment.serializers import OrderItemSerializer


class OrderItemSerializerTest(TestCase):

    def test_valid_serializer(self):
        data = {
            "product_name": "Laptop",
            "quantity": 2
        }

        serializer = OrderItemSerializer(data=data)

        self.assertTrue(serializer.is_valid())

    def test_invalid_serializer(self):
        data = {
            "quantity": 2
        }

        serializer = OrderItemSerializer(data=data)

        self.assertFalse(serializer.is_valid())