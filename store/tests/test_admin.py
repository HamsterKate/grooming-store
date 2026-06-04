from django.test import TestCase
from django.contrib.admin.sites import site
from store.models import Groomer, Pet, Service


class AdminTest(TestCase):

    def test_models_registered(self):
        self.assertIn(Groomer, site._registry)
        self.assertIn(Pet, site._registry)
        self.assertIn(Service, site._registry)
