from django.http import HttpResponse
from django.template import loader
from .models import Pokemon
from django.shortcuts import render #Clase Entrenador
from .models import Entrenador #Clase Entrenador

def index(request):
    pokemons = Pokemon.objects.all()
    template = loader.get_template('index.html')
    return HttpResponse(template.render({'pokemons': pokemons}, request))

def pokemon(request, pokemon_id):
    pokemon = Pokemon.objects.get(id = pokemon_id)
    template = loader.get_template('display_pokemon.html')
    context = {
        'pokemon': pokemon
    }
    return HttpResponse(template.render(context, request))

#Clase Entrenador
def lista_entrenadores(request):
    entrenadores = Entrenador.objects.all()
    return render(request, 'lista.html', {'entrenadores': entrenadores})