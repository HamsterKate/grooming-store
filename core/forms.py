from django import forms


class SearchForm(forms.Form):
    query = forms.CharField(
        max_length=100,
        required=False,
        label="",
        widget=forms.TextInput(attrs={
            "class": "form-control form-control-sm h-100",
            "placeholder": "Search..."
        }),
    )

    field = forms.ChoiceField(
        required=False,
        label="",
        widget=forms.Select(attrs={
            "class": "form-select form-select-sm h-100"
        })
    )

    def __init__(self, *args, **kwargs):
        fields_choices = kwargs.pop("fields_choices", [])
        show_field = kwargs.pop("show_field", True)

        super().__init__(*args, **kwargs)

        if show_field:
            self.fields["field"].choices = fields_choices
        else:
            # на index сторінці прибираємо field
            self.fields.pop("field")
