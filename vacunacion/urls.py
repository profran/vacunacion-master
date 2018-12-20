from django.urls import path
from .views import add_vaccination, create_carnet, carnet_detail, get_carnet

urlpatterns = [
    path('carnet/add/<str:query>', add_vaccination, name='add_vaccination'),
    path('carnet/create', create_carnet, name='create_carnet'),
    path('carnet/<int:carnet_id>', carnet_detail, name='carnet_detail'),
    path('carnet/add', get_carnet, name='get_carnet'),
]
