from email import message
from django.contrib import messages
from django.shortcuts import get_object_or_404, render, redirect

from .api.pokeapi import poke_api
from .models import Pokemon



def criarpokemon(request):
    if request.method == 'POST':
        pokemonstrinhos = request.POST['pokemonzinho']
        if Pokemon.objects.filter(nome=pokemonstrinhos).exists():
            messages.error(request, 'O pokemon já existe no banco de dados')
            return redirect('visualizar_pokemon')
        poke_api(pokemonstrinhos)
        if not Pokemon.objects.filter(nome=pokemonstrinhos).exists():
            messages.error(request, 'O pokemon não existe')
            return redirect('criarpokemon')
        if Pokemon.objects.filter(nome=pokemonstrinhos).exists():
            messages.success(request, 'O pokemon foi criado com sucesso')
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
    return render(request, 'busca.html', dados)

        
def visualizar_pokemon(request):
    pokemon = Pokemon.objects.order_by('nome')
    conteudo = {
        'pokemon' : pokemon
    }
    return render(request, 'visualizar_pokemon.html', conteudo)

def visualizar_apenas_pokemon(request, slug):
    pokemonstro = get_object_or_404(Pokemon, slug=slug)
    visualizar_pokemon = {
        'poke' : pokemonstro
    }
    return render(request, 'visualizar_apenas_pokemon.html', visualizar_pokemon)