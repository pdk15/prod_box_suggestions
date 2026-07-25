from rest_framework.test import APITestCase
from rest_framework import status


class ProductViewTest(APITestCase):

    def test_product_list(self):

        response = self.client.get("/api/products/")

        self.assertEqual(response.status_code, status.HTTP_200_OK)


class BoxViewTest(APITestCase):

    def test_box_list(self):

        response = self.client.get("/api/boxes/")

        self.assertEqual(response.status_code, status.HTTP_200_OK)