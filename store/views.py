from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from store.forms import PetForm, GroomerForm, ServiceForm
from store.models import Groomer, Service, Pet
from core.mixins import SearchMixin


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


class GroomerListView(SearchMixin, generic.ListView):
    model = Groomer
    context_object_name = "groomers"
    paginate_by = 2


class GroomerDetailView(generic.DetailView):
    model = Groomer


class GroomerCreateView(LoginRequiredMixin, generic.CreateView):
    model = Groomer
    form_class = GroomerForm
    template_name = "store/groomer_form.html"
    success_url = reverse_lazy("store:groomer-list")


class GroomerUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Groomer
    form_class = GroomerForm
    template_name = "store/groomer_form.html"
    success_url = reverse_lazy("store:groomer-list")


class GroomerDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Groomer
    template_name = "store/groomer_confirm_delete.html"
    success_url = reverse_lazy("store:groomer-list")


class ServiceListView(SearchMixin, generic.ListView):
    model = Service
    queryset = Service.objects.all()
    context_object_name = "services"
    paginate_by = 2


class ServiceDetailView(generic.DetailView):
    model = Service


class ServiceCreateView(LoginRequiredMixin, generic.CreateView):
    model = Service
    form_class = ServiceForm
    template_name = "store/service_form.html"
    success_url = reverse_lazy("store:service-list")


class ServiceUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Service
    form_class = ServiceForm
    template_name = "store/service_form.html"
    success_url = reverse_lazy("store:service-list")


class ServiceDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Service
    template_name = "store/service_confirm_delete.html"
    success_url = reverse_lazy("store:service-list")


class PetListView(LoginRequiredMixin, SearchMixin, generic.ListView):
    model = Pet
    queryset = Pet.objects.select_related("groomer").prefetch_related(
        "services", "petservice_set"
    )
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


class PetCreateView(LoginRequiredMixin, generic.CreateView):
    model = Pet
    form_class = PetForm
    template_name = "store/pet_form.html"
    success_url = reverse_lazy("store:pet-list")

    def form_valid(self, form):
        form.instance.groomer = self.request.user.groomer_profile
        return super().form_valid(form)

    def form_invalid(self, form):
        print(form.errors)
        return super().form_invalid(form)


class PetUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Pet
    form_class = PetForm
    template_name = "store/pet_form.html"
    success_url = reverse_lazy("store:pet-list")


class PetDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Pet
    template_name = "store/pet_confirm_delete.html"
    success_url = reverse_lazy("store:pet-list")
