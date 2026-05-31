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
    paginate_by = 10


class ServiceView(generic.ListView):
    model = Service
    queryset = Service.objects.all()
    paginate_by = 10


class PetView(generic.ListView):
    model = Pet
    queryset = Pet.objects.select_related("groomer").prefetch_related("services")
    paginate_by = 10
