from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Groomer

User = get_user_model()


@receiver(post_save, sender=User)
def create_groomer(sender, instance, created, **kwargs):
    if created:
        Groomer.objects.create(
            user=instance,
            first_name=instance.username,
            last_name=""
        )
