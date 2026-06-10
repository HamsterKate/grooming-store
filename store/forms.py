from django import forms
from .models import Pet, Groomer, Service


class BaseStyledForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs.update({
                "class": "form-control"
            })


class PetForm(BaseStyledForm):
    class Meta:
        model = Pet
        fields = ["name", "species", "breed", "services"]

    def clean_name(self):
        name = self.cleaned_data["name"]
        if len(name.strip()) < 2:
            raise forms.ValidationError("Pet name too short")
        return name


class GroomerForm(BaseStyledForm):
    class Meta:
        model = Groomer
        fields = ["first_name", "last_name", "qualifications"]

    def clean_first_name(self):
        name = self.cleaned_data["first_name"]
        if len(name.strip()) < 2:
            raise forms.ValidationError("First name too short")
        return name

    def clean_last_name(self):
        name = self.cleaned_data["last_name"]
        if len(name.strip()) < 2:
            raise forms.ValidationError("Last name too short")
        return name


class ServiceForm(BaseStyledForm):
    class Meta:
        model = Service
        fields = ["name", "service_type", "description"]

    def clean_name(self):
        name = self.cleaned_data["name"]
        if len(name.strip()) < 3:
            raise forms.ValidationError("Service name too short")
        return name
