from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from accounts.models import CarnetOwner


# Create your models here.

class Vaccine(models.Model):
    name = models.CharField(max_length=40, null=False, blank=False)


class Carnet(models.Model):
    owner = models.OneToOneField(CarnetOwner, on_delete=models.CASCADE, related_name='carnet')
    date_created = models.DateTimeField(auto_now_add=True)


class Vaccination(models.Model):
    carnet = models.ForeignKey(Carnet, on_delete=models.CASCADE, related_name='vaccinations')
    vaccine = models.OneToOneField(Vaccine, on_delete=models.CASCADE, unique=True)
    unique = models.BooleanField(default=False)


class Dose(models.Model):
    TYPE_CHOICES = {
        ('1', 'First'),
        ('2', 'Second'),
        ('3', 'Third'),
        ('4', 'Fourth'),
        ('5', 'Fifth'),
        ('r', 'Reinforcement'),
        ('o', 'Opcional')

    }

    vaccination = models.ForeignKey(Vaccination, on_delete=models.CASCADE, default=None, related_name='doses')
    type = models.CharField(max_length=1, choices=TYPE_CHOICES, null=False, blank=False)
    medic = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

@receiver(post_save, sender=CarnetOwner)
def create_carnet(sender, instance, **kwargs):
    carnet = Carnet.objects.get_or_create(owner=instance)
