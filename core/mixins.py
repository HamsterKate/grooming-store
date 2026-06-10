from django.db.models import Q

from core.search_registry import FIELD_LOOKUP


class SearchMixin:
    search_view_name = None

    def get_queryset(self):
        queryset = super().get_queryset()

        query = self.request.GET.get("query")
        field = self.request.GET.get("field")

        # 🏠 GLOBAL SEARCH (index page)
        if self.search_view_name == "index" and query:
            return queryset.filter(
                Q(first_name__icontains=query) |
                Q(last_name__icontains=query) |
                Q(name__icontains=query) |
                Q(breed__icontains=query)
            )

        # 📄 LOCAL SEARCH (list pages)
        if query and field:
            lookup = FIELD_LOOKUP.get(field)

            if lookup:
                queryset = queryset.filter(
                    Q(**{lookup: query})
                )

        return queryset
