from core.forms import SearchForm
from core.search_registry import SEARCH_FIELDS


def search_form(request):
    view_name = getattr(request.resolver_match, "url_name", "")

    fields_choices = SEARCH_FIELDS.get(view_name, [
        ("first_name", "Name"),
    ])

    form = SearchForm(request.GET or None, fields_choices=fields_choices)

    return {"search_form": form}
