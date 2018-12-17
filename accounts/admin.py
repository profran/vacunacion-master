from django.contrib import admin
from .models import User, MedicProfile

# Register your models here.

admin.site.register((User, MedicProfile))