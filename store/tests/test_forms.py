from django.test import TestCase
from store.forms import GroomerForm


class GroomerFormTest(TestCase):

    def test_valid_form(self):
        form = GroomerForm(data={
            "first_name": "Anna",
            "last_name": "Kovalenko",
        })

        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        form = GroomerForm(data={})
        self.assertFalse(form.is_valid())
