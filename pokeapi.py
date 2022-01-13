import requests

def foto(pokemon):
    global foto_do_pokemon
    foto_do_pokemon = pokemon['sprites']['front_default']
    

def nomes(pokemon):
    global nome
    nome = pokemon['name']
    
def pokedex(pokemon):
    lista = []
    global pokedex_do_jogo
    for i in pokemon['game_indices']:
        numero_da_pokedex = str(i['game_index'])
        jogo = i['version']['name']
        numero_da_pokedex_no_jogo = numero_da_pokedex + ' : ' + jogo
        lista.append(numero_da_pokedex_no_jogo)
    pokedex_do_jogo = lista[0]
    
def habilidade(pokemon):
    lista = []
    global habilidade0
    global habilidade1
    for i in pokemon['abilities']:
        habilidade_do_pokemon = i['ability']['name']
        lista.append(habilidade_do_pokemon)
    habilidade0 = lista[0]
    if len(lista) > 1:
        habilidade1 = lista[1]

def altura(pokemon):
    global altura_pokemon
    altura_pokemon = pokemon['height']

def statisticas(pokemon):
    lista = []
    global statistica0
    global statistica1
    global statistica2
    global statistica3
    global statistica4
    global statistica5
    for i in pokemon['stats']:
        status_base = str(i['base_stat'])
        nome_status = i['stat']['name']
        status_do_pokemon = nome_status + " : " + status_base
        lista.append(status_do_pokemon)
    statistica0 = lista[0]
    statistica1 = lista[1]
    statistica2 = lista[2]
    statistica3 = lista[3]
    statistica4 = lista[4]
    statistica5 = lista[5]


def tipo(pokemon):
    lista = []
    global tipo0
    global tipo0
    for i in pokemon['types']:
        nome_do_tipo = i['type']['name']
        lista.append(nome_do_tipo)
    tipo0 = lista[0]
    
    if len(lista) > 1:
        tipo1 = lista[1]
        
        
        
def poke_api():
    url = 'https://pokeapi.co/api/v2/pokemon/haunter'
    res = requests.get(url)
    status = res.status_code
    if status == 200:
        pokemon = res.json()
        foto(pokemon)
        nomes(pokemon)
        pokedex(pokemon)      
        habilidade(pokemon)      
        altura(pokemon)
        statisticas(pokemon)
        tipo(pokemon)
              
    else:
        print('codigo errado')


poke_api()