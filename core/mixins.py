from django.db.models import Q
from core.search_registry import FIELD_LOOKUP


class SearchMixin:
    search_view_name = None  # будемо задавати в view

    def get_queryset(self):
        queryset = super().get_queryset()

        query = self.request.GET.get("query")
        field = self.request.GET.get("field")

        if query and field:
            lookup = FIELD_LOOKUP.get(field)

            if lookup:
                queryset = queryset.filter(
                    Q(**{lookup: query})
                )

        return queryset
