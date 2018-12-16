from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):
    is_medic = models.BooleanField(null=True)
    dni = models.CharField(max_length=9, null=True, blank=False, unique=True)
    born_date = models.DateField(null=True)


class MedicProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    plate = models.CharField(max_length=8, null=False, blank=False, unique=True)


class CarnetOwner(models.Model):
    user = models.ForeignKey(User, null=False, on_delete=models.CASCADE, related_name='childs')
    name = models.CharField(max_length=15, null=False, blank=False)
    last_name = models.CharField(max_length=15, null=False, blank=False)
    dni = models.CharField(max_length=9, null=True, blank=False)
    born_date = models.DateField(null=True)


@receiver(post_save, sender=User)
def create_carnet_owner(sender, instance, **kwargs):
    carnet_owner = CarnetOwner.objects.get_or_create(user=instance, dni=instance.dni, name=instance.first_name, last_name=instance.last_name)
