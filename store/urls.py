from django.urls import path

from store import views

app_name = "store"
urlpatterns = [
    path("", views.index, name="index"),
    path("groomers/", views.GroomerView.as_view(), name="groomers"),
    path("pets/", views.PetView.as_view(), name="pets"),
    path("services/", views.ServiceView.as_view(), name="services"),
]
