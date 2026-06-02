from django import forms


class SearchForm(forms.Form):
    query = forms.CharField(
        max_length=100,
        required=False,
        label="",
        widget=forms.TextInput(attrs={
            "class": "form-control form-control-sm",
            "placeholder": "Search..."
        }),
    )

    field = forms.ChoiceField(
        required=False,
        label="",
    )

    def __init__(self, *args, **kwargs):
        fields_choices = kwargs.pop("fields_choices", [])

        super().__init__(*args, **kwargs)
        self.fields["field"].choices = fields_choices
