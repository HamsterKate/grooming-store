from django.contrib import admin
from .models import Service, Groomer, Pet, Qualification


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("name", "service_type", "description",)
    list_filter = ("service_type",)
    search_fields = ("name",)
    ordering = ("name",)


@admin.register(Qualification)
class QualificationAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(Groomer)
class GroomerAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "show_qualifications")
    search_fields = ("first_name", "last_name")
    filter_horizontal = ("qualifications",)

    def show_qualifications(self, obj):
        return ", ".join(q.name for q in obj.qualifications.all())

    show_qualifications.short_description = "Qualifications"


@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ("name", "species", "breed", "groomer")
    search_fields = ("name", "species", "breed")
    list_filter = ("species", "groomer", "services")
    autocomplete_fields = ("groomer", "services")

