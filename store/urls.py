from django.urls import path

from store import views

app_name = "store"
urlpatterns = [
    path("", views.index, name="index"),
    path("groomers/", views.GroomerView.as_view(), name="groomer-list"),
    path("pets/", views.PetView.as_view(), name="pet-list"),
    path("services/", views.ServiceView.as_view(), name="service-list"),
]
