from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser
import random
import string


# Create your models here.

class User(AbstractUser):
    is_medic = models.BooleanField(null=True)
    dni = models.CharField(max_length=9, null=True, blank=False, unique=True)
    born_date = models.DateField(null=True)


class MedicProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    plate = models.CharField(max_length=8, null=False, blank=False, unique=True)


class Token(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='token')
    token = models.CharField(max_length=6, null=False)
    attemps = models.IntegerField(null=False, default=0)

    @staticmethod
    def create_token():
        return ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(6))

    def reset(self):
        self.token = self.create_token()
        self.attemps = 0


@receiver(post_save, sender=User)
def create_carnet(sender, instance, **kwargs):
    Token.objects.get_or_create(user=instance, defaults={'token': Token.create_token()})
