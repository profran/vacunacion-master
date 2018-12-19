from django.urls import path
from .views import add_vaccination, create_carnet, carnet_detail

urlpatterns = [
    path('carnet/add/<str:query>', add_vaccination, name='add_vaccination'),
    path('carnet/create', create_carnet, name='create_carnet'),
    path('carnet/<int:carnet_id>', carnet_detail, name='carnet_detail')
]
