from django.test import TestCase
from shipment.models import Product, ShippingBox


class ProductModelTest(TestCase):

    def test_create_product(self):
        product = Product.objects.create(
            name="Laptop",
            length=30,
            width=20,
            height=5,
            weight=2
        )

        self.assertEqual(product.name, "Laptop")
        self.assertEqual(product.weight, 2)


class ShippingBoxModelTest(TestCase):

    def test_create_box(self):
        box = ShippingBox.objects.create(
            name="Small Box",
            inner_length=40,
            inner_width=30,
            inner_height=20,
            max_weight=10,
            cost=100
        )

        self.assertEqual(box.name, "Small Box")
        self.assertEqual(box.cost, 100)