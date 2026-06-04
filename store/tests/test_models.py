from django.test import TestCase
from store.models import Groomer, Pet, Service, Qualification


class GroomerModelTest(TestCase):

    def setUp(self):
        self.groomer = Groomer.objects.create(
            first_name="Anna",
            last_name="Kovalenko",
        )

    def test_str(self):
        self.assertEqual(str(self.groomer), "Anna Kovalenko")
