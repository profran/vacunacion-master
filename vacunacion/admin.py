from django.contrib import admin
from .models import Vaccine, Vaccination, Dose, Carnet

# Register your models here.

admin.site.register((Vaccine, Vaccination, Dose, Carnet))