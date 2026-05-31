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


class GroomerView(generic.ListView):
    model = Groomer
    queryset = Groomer.objects.all()
    context_object_name = "groomers"
    paginate_by = 10


class GroomerDetailView(generic.DetailView):
    model = Groomer


class ServiceView(generic.ListView):
    model = Service
    queryset = Service.objects.all()
    context_object_name = "services"
    paginate_by = 10


class ServiceDetailView(generic.DetailView):
    model = Service


class PetView(generic.ListView):
    model = Pet
    queryset = Pet.objects.select_related("groomer").prefetch_related("services")
    context_object_name = "pets"
    paginate_by = 10


class PetDetailView(generic.DetailView):
    model = Pet
    queryset = Pet.objects.select_related("groomer").prefetch_related("services")
