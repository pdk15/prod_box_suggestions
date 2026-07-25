from rest_framework.test import APITestCase
from shipment.models import Product, ShippingBox


class RecommendBoxAPITest(APITestCase):

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

    def test_recommend_box_api(self):

        payload = {
    "items": [
        {
            "product_name": "Laptop",
            "quantity": 2
        }
    ]
}

        response = self.client.post(
            "/api/recommend-box/",
            payload,
            format="json"
        )

        self.assertEqual(response.status_code, 200)