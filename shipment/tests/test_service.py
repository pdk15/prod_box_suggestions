from django.test import TestCase
from shipment.models import Product, ShippingBox
from shipment.services import recommend_box


class RecommendBoxServiceTest(TestCase):

    def setUp(self):
        self.product = Product.objects.create(
            name="Laptop",
            length=30,
            width=20,
            height=5,
            weight=2
        )

        ShippingBox.objects.create(
            name="Small Box",
            inner_length=40,
            inner_width=30,
            inner_height=20,
            max_weight=10,
            cost=100
        )

    def test_recommend_box(self):

        items = [
    {
        "product_name": "Laptop",
        "quantity": 2
    }
]

        box = recommend_box(items)

        self.assertIsNotNone(box)
        self.assertEqual(box.name, "Small Box")