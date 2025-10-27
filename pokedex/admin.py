from django.contrib import admin
from .models import Pokemon
from .models import Entrenador #Clase Entrenador


# Register your models here.
@admin.register(Pokemon)
class PokemonAdmin(admin.ModelAdmin):
    pass

admin.site.register(Entrenador) #Clase Entrenador 
