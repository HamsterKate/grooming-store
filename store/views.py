from django.shortcuts import render
from django.views import generic

from store.models import Groomer, Service, Pet


# Create your views here.
def index(request):
    num_groomers = Groomer.objects.count()
    num_services = Service.objects.count()
    num_pets = Pet.objects.count()

    context = {
        "num_groomers": num_groomers,
        "num_services": num_services,
        "num_pets": num_pets,
    }
    return render(
        request,
        "store/index.html",
        context=context,
    )


class GroomerListView(generic.ListView):
    model = Groomer
    queryset = Groomer.objects.all()
    context_object_name = "groomers"
    paginate_by = 2

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["search_fields"] = [
            ("name", "Name"),
            ("specialization", "Specialization"),
        ]

        return context


class GroomerDetailView(generic.DetailView):
    model = Groomer


class ServiceListView(generic.ListView):
    model = Service
    queryset = Service.objects.all()
    context_object_name = "services"
    paginate_by = 2


class ServiceDetailView(generic.DetailView):
    model = Service


class PetListView(generic.ListView):
    model = Pet
    queryset = Pet.objects.select_related("groomer").prefetch_related("services", "petservice_set")
    context_object_name = "pets"
    paginate_by = 10


class PetDetailView(generic.DetailView):
    model = Pet
    queryset = Pet.objects.select_related("groomer").prefetch_related(
        "services",
        "petservice_set__service",
        "petservice_set__groomer",
    )
    context_object_name = "pet"
