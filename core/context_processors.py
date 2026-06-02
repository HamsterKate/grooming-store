from core.forms import SearchForm


def search_form(request):
    form = SearchForm(
        request.GET or None,
        fields_choices=[
            ("name", "Name"),
        ],
    )

    return {
        "search_form": form
    }
