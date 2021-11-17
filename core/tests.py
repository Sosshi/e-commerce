from django.test import TestCase


class MainPagetest(TestCase):
    def test_homepage_view(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
