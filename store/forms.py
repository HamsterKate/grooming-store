from django import forms
from .models import Pet, Groomer, Service


class PetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ["name", "species", "breed", "services"]


class GroomerForm(forms.ModelForm):
    class Meta:
        model = Groomer
        fields = ["first_name", "last_name", "qualifications"]


class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ["name", "service_type", "description"]
