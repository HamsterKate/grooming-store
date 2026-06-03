from django.urls import path, include

from store import views

app_name = "store"

urlpatterns = [
    path("", views.index, name="index"),
    path("groomers/", views.GroomerListView.as_view(), name="groomer-list"),
    path(
        "groomers/<int:pk>/", views.GroomerDetailView.as_view(), name="groomer-detail"
    ),
    path("pets/", views.PetListView.as_view(), name="pet-list"),
    path("pets/<int:pk>/", views.PetDetailView.as_view(), name="pet-detail"),
    path("services/", views.ServiceListView.as_view(), name="service-list"),
    path(
        "services/<int:pk>/", views.ServiceDetailView.as_view(), name="service-detail"
    ),
    path("pets/create/", views.PetCreateView.as_view(), name="pet-create"),
    path("pets/<int:pk>/update/", views.PetUpdateView.as_view(), name="pet-update"),
    path("pets/<int:pk>/delete/", views.PetDeleteView.as_view(), name="pet-delete"),
    path("groomers/create/", views.GroomerCreateView.as_view(), name="groomer-create"),
    path("groomers/<int:pk>/update/", views.GroomerUpdateView.as_view(), name="groomer-update"),
    path("groomers/<int:pk>/delete/", views.GroomerDeleteView.as_view(), name="groomer-delete"),
    path("services/create/", views.ServiceCreateView.as_view(), name="service-create"),
    path("services/<int:pk>/update/", views.ServiceUpdateView.as_view(), name="service-update"),
    path("services/<int:pk>/delete/", views.ServiceDeleteView.as_view(), name="service-delete"),
]
