from django.conf import settings

from core.forms import SearchForm
from core.search_registry import SEARCH_FIELDS


def search_form(request):
    view_name = getattr(request.resolver_match, "url_name", "")

    fields_choices = SEARCH_FIELDS.get(view_name, [])

    is_home = (view_name == "index")

    form = SearchForm(
        request.GET or None,
        fields_choices=fields_choices,
        show_field=not is_home
    )

    return {
        "search_form": form,
        "is_home": is_home
    }


def cfg_assets_root(request):
    return {
        "ASSETS_ROOT":
                getattr(settings,
                        "ASSETS_ROOT",
                        "/static/assets")
    }
