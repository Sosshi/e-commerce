from django.test import TestCase


class ProductsTestCase(TestCase):
    def test_product_list_view(self):
        response = self.client.get("/products/")
        self.assertEqual(response.status_code, 200)
