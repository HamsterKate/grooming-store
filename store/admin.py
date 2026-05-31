from django.contrib import admin
from .models import Service, Groomer, Pet


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("name", "service_type")
    list_filter = ("service_type",)
    search_fields = ("name",)
    ordering = ("name",)


@admin.register(Groomer)
class GroomerAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "qualification", "created_at")
    search_fields = ("first_name", "last_name", "qualification")
    list_filter = ("qualification",)
    ordering = ("first_name", "last_name")


@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ("name", "species", "breed", "groomer")
    search_fields = ("name", "species", "breed")
    list_filter = ("species", "groomer", "services")
    autocomplete_fields = ("groomer", "services")
