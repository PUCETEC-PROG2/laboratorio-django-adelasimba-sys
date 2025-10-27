from django.urls import path
from . import views #Clase Entrenador

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:pokemon_id>/", views.pokemon, name="pokemon"),
    path('entrenadores/', views.lista_entrenadores, name='entrenadores'),

]