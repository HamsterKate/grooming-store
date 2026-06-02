from django.urls import path, include

from store import views

app_name = "store"
urlpatterns = [
    path("", views.index, name="index"),
    path("groomers/", views.GroomerListView.as_view(), name="groomer-list"),
    path("groomers/<int:pk>/", views.GroomerDetailView.as_view(), name="groomer-detail"),
    path("pets/", views.PetListView.as_view(), name="pet-list"),
    path("pets/<int:pk>/", views.PetDetailView.as_view(), name="pet-detail"),
    path("services/", views.ServiceListView.as_view(), name="service-list"),
    path("services/<int:pk>/", views.ServiceDetailView.as_view(), name="service-detail"),
    path("accounts/", include("django.contrib.auth.urls"), name="accounts"),
]
