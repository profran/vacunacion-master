from django.contrib import admin
from .models import User, MedicProfile, CarnetOwner

# Register your models here.

admin.site.register((User, MedicProfile, CarnetOwner))