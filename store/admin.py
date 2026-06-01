from django.contrib import admin
from .models import Service, Groomer, Pet, Qualification, PetService


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


class PetServiceInline(admin.TabularInline):
    model = PetService
    extra = 1
    autocomplete_fields = ("service", "groomer")


@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ("name", "species", "breed", "groomer", "show_services")

    def show_services(self, obj):
        return ", ".join(p.service.name for p in obj.petservice_set.all())

    show_services.short_description = "Services"
    search_fields = ("name", "species", "breed")
    list_filter = ("species", "groomer", "services")
    autocomplete_fields = ("groomer", "services")
    inlines = [PetServiceInline]


@admin.register(PetService)
class PetServiceAdmin(admin.ModelAdmin):
    list_display = ("pet", "service", "groomer", "date", "created_at")
    list_filter = ("service", "groomer", "date")
    search_fields = ("pet__name", "service__name", "groomer__first_name")
    autocomplete_fields = ("pet", "service", "groomer")



