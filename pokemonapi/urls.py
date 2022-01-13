from django.urls import path
from pokemonapi import views


urlpatterns = [
    path('criarpokemon/', views.criarpokemon, name='criarpokemon'),
    path('', views.visualizar_pokemon, name='visualizar_pokemon'),
    path('buscar/' , views.buscar, name='buscar')
]