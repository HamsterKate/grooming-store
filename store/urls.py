from django.urls import path

from store import views

app_name = "store"
urlpatterns = [
    path("", views.index, name="index"),
    path("groomers/", views.GroomerView.as_view(), name="groomer-list"),
    path("groomers/<int:pk>/", views.GroomerDetailView.as_view(), name="groomer-detail"),
    path("pets/", views.PetView.as_view(), name="pet-list"),
    path("services/", views.ServiceView.as_view(), name="service-list"),
    path("services/<int:pk>/", views.ServiceDetailView.as_view(), name="service-detail"),
]
