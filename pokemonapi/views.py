from django.shortcuts import get_object_or_404, render, redirect

from .api.pokeapi import poke_api
from .models import Pokemon



def criarpokemon(request):
    if request.method == 'POST':
        pokemonstrinhos = request.POST['pokemonzinho']
        poke_api(pokemonstrinhos)
        return redirect('visualizar_pokemon')
    return render(request, 'criarpokemon.html')

def buscar(request):
    lista_a_buscar = Pokemon.objects.order_by('nome')
    if 'buscar' in request.GET:
        nome_buscado = request.GET['buscar']
        if buscar:
            lista_a_buscar = lista_a_buscar.filter(nome__icontains= nome_buscado)
    dados = {
        'pokemon': lista_a_buscar
    }
    return render(request, 'visualizar_apenas_pokemon.html', dados)

        
def visualizar_pokemon(request):
    pokemon = Pokemon.objects.order_by('nome')
    conteudo = {
        'pokemon' : pokemon
    }
    return render(request, 'visualizar_pokemon.html', conteudo)