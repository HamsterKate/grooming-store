from django.db import models


class Service(models.Model):

    class ServiceType(models.TextChoices):
        BASIC = "basic", "Basic"
        FULL = "full", "Full grooming"
        SPA = "spa", "Spa"
        OTHER = "other", "Other"

    name = models.CharField(
        max_length=100,
        unique=True,
    )
    service_type = models.CharField(
        max_length=20,
        choices=ServiceType,
        default=ServiceType.BASIC,
    )
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "services"
        verbose_name = "Service"
        verbose_name_plural = "Services"
        ordering = ["name"]


class Qualification(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "qualifications"
        verbose_name = "Qualification"
        verbose_name_plural = "Qualifications"
        ordering = ["name"]


class Groomer(models.Model):
    first_name = models.CharField(
        max_length=50,
    )
    last_name = models.CharField(
        max_length=50,
    )
    qualifications= models.ManyToManyField(
        Qualification,
        related_name="groomers",
        blank=True,
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        db_table = "groomers"
        verbose_name = "Groomer"
        verbose_name_plural = "Groomers"
        ordering = [
            "first_name",
            "last_name",
        ]


class Pet(models.Model):
    name = models.CharField(
        max_length=50,
    )
    species = models.CharField(
        max_length=100,
    )
    breed = models.CharField(
        max_length=100,
        blank=True,
        default="",
    )
    groomer = models.ForeignKey(
        Groomer,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="pets",
    )
    services = models.ManyToManyField(
        Service,
        blank=True,
        related_name="pets"
    )

    class Meta:
        db_table = "pets"
        verbose_name = "Pet"
        verbose_name_plural = "Pets"
        ordering = ["name"]

    def __str__(self):
        return self.name


class PetService(models.Model):
    pet = models.ForeignKey("Pet", on_delete=models.CASCADE)
    service = models.ForeignKey("Service", on_delete=models.CASCADE)
    groomer = models.ForeignKey("Groomer", on_delete=models.SET_NULL, null=True, blank=True)

    date = models.DateTimeField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.pet.name} - {self.service.name} ({self.date})"
