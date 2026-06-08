from django.test import TestCase
from django.urls import reverse
from store.models import Groomer


class GroomerSearchTest(TestCase):

    def setUp(self):
        self.g1 = Groomer.objects.create(
            first_name="Anna",
            last_name="Kovalenko",
        )
        self.g2 = Groomer.objects.create(
            first_name="John",
            last_name="Smith",
        )

    def test_search_by_first_name(self):
        url = reverse("store:groomer-list")

        response = self.client.get(url, {
            "query": "Anna",
            "field": "first_name"
        })

        self.assertContains(response, "Anna")
        self.assertNotContains(response, "John")

    def test_search_by_last_name(self):
        url = reverse("store:groomer-list")

        response = self.client.get(url, {
            "query": "Smith",
            "field": "last_name"
        })

        self.assertContains(response, "John")
        self.assertNotContains(response, "Anna")

    def test_empty_search_returns_all(self):
        url = reverse("store:groomer-list")

        response = self.client.get(url)

        self.assertContains(response, "Anna")
        self.assertContains(response, "John")

