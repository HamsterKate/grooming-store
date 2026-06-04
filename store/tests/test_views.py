from django.test import TestCase
from django.urls import reverse
from store.models import Groomer


class GroomerViewsTest(TestCase):

    def setUp(self):
        self.groomer = Groomer.objects.create(
            first_name="Anna",
            last_name="Kovalenko",
        )

    def test_list_view(self):
        url = reverse("store:groomer-list")
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Anna")

    def test_detail_view(self):
        url = reverse("store:groomer-detail", args=[self.groomer.pk])
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Anna")
