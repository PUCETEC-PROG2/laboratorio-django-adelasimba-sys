from django.http import HttpResponse
from django.template import loader
from .models import Pokemon, Trainer
from django.shortcuts import redirect, render
from pokedex.forms import PokemonForm, TrainerForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404


def index(request):
    pokemons = Pokemon.objects.all()
    trainers = Trainer.objects.all()

    template = loader.get_template('index.html')
    return HttpResponse(template.render({'pokemons': pokemons, 'trainers': trainers}, request))

def pokemon(request, pokemon_id):
    pokemon = Pokemon.objects.get(id = pokemon_id)
    template = loader.get_template('display_pokemon.html')
    context = {
        'pokemon': pokemon
    }
    return HttpResponse(template.render(context, request))


def trainers(request):
    trainers = Trainer.objects.all() 
    return render(request, 'trainers.html', {'trainers': trainers})

def trainer_display(request, trainer_id):
    trainer = get_object_or_404(Trainer, id=trainer_id)
    return render(request, "trainer_detail.html", {"trainer": trainer})


@login_required
def add_trainer(request):
    form = TrainerForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect("pokedex:trainers")
    return render(request, "trainer_form.html", {"form": form})

@login_required
def edit_trainer(request, id):
    trainer = get_object_or_404(Trainer, id=id)
    form = TrainerForm(request.POST or None, request.FILES or None, instance=trainer)
    if form.is_valid():
        form.save()
        return redirect("pokedex:trainers")
    return render(request, "trainer_form.html", {"form": form})

@login_required
def delete_trainer(request, id):
    trainer = get_object_or_404(Trainer, id=id)
    trainer.delete()
    return redirect("pokedex:trainers")

@login_required
def add_pokemon(request):
    if request.method =="POST":
        form= PokemonForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('pokedex:index')
    else:
        form= PokemonForm()
    return render(request, 'pokemon_form.html', {'form': form})

@login_required
def edit_pokemon(request, pokemon_id):
    pokemon = Pokemon.objects.get(id = pokemon_id)
    if request.method =="POST":
        form= PokemonForm(request.POST, request.FILES, instance=pokemon)
        if form.is_valid():
            form.save()
            return redirect('pokedex:index')
    else:
        form= PokemonForm(instance=pokemon)
    return render(request, 'pokemon_form.html', {'form': form})

@login_required
def delete_pokemon(request, pokemon_id):
    pokemon = Pokemon.objects.get(id = pokemon_id)
    pokemon.delete()
    return redirect('pokedex:index')

class CustomLoginView(LoginView):
    template_name="login_form.html"