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
