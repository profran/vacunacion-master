from django.urls import path
from .views import add_vaccination, create_carnet

urlpatterns = [
    path('carnet/add/<str:query>', add_vaccination, name='add_vaccination'),
    path('carnet/create', create_carnet, name='create_carnet')
]
