from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from accounts.models import User


# Create your models here.

class Vaccine(models.Model):
    name = models.CharField(max_length=40, null=False, blank=False)

    def __str__(self):
        return (self.name)

class Carnet(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, null=False, on_delete=models.CASCADE, related_name='carnets')
    name = models.CharField(max_length=15, null=False, blank=False)
    last_name = models.CharField(max_length=15, null=False, blank=False)
    dni = models.CharField(max_length=9, null=True, blank=False)
    born_date = models.DateField(null=True)

    def __str__(self):
        return (self.name + ', ' + self.last_name)


class Vaccination(models.Model):
    carnet = models.ForeignKey(Carnet, on_delete=models.CASCADE, related_name='vaccinations')
    vaccine = models.ForeignKey(Vaccine, on_delete=models.CASCADE, related_name='vaccine')


class Dose(models.Model):
    TYPE_CHOICES = {
        ('1', 'Primera dosis'),
        ('2', 'Segunda dosis'),
        ('3', 'Tercer dosis'),
        ('4', 'Cuarta dosis'),
        ('5', 'Quinta dosis'),
        ('r', 'Refuerzo'),
        ('u', 'Unica')

    }

    vaccination = models.ForeignKey(Vaccination, on_delete=models.CASCADE, default=None, related_name='doses')
    type = models.CharField(max_length=1, choices=TYPE_CHOICES, null=False, blank=False)
    medic = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='doses')
    date = models.DateField(null=False)
    next_dose = models.DateField(null=True)
    batch_number = models.CharField(max_length=15, null=False, blank=False)


@receiver(post_save, sender=User)
def create_carnet(sender, instance, **kwargs):
    carnet= Carnet.objects.get_or_create(user=instance, dni=instance.dni, name=instance.first_name,
                                                last_name=instance.last_name)
