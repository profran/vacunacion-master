from django.contrib import admin
from .models import User, MedicProfile, Token

# Register your models here.

admin.site.register((User, MedicProfile, Token))