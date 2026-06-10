from django.conf import settings

from core.forms import SearchForm
from core.search_registry import SEARCH_FIELDS


def search_form(request):
    view_name = getattr(request.resolver_match, "url_name", "")

    fields_choices = SEARCH_FIELDS.get(view_name, [])

    is_list_page = view_name.endswith("-list")

    form = SearchForm(
        request.GET or None,
        fields_choices=fields_choices,
        show_field=is_list_page
    )

    return {
        "search_form": form if is_list_page else None,
        "is_list_page": is_list_page
    }


def cfg_assets_root(request):
    return {
        "ASSETS_ROOT":
                getattr(settings,
                        "ASSETS_ROOT",
                        "/static/assets")
    }
