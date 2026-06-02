from store.forms import SearchForm


def search_form(request):
    form = SearchForm(request.GET or None)

    return {
        "search_form": form
    }
