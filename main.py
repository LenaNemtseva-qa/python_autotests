import requests

token = '65d77ea6bea31a4c2af203a7e4cbb077'
add_pokemon = requests.post('https://pokemonbattle.me:9104/pokemons', 
              headers ={'trainer_token':token, 'Content-Type':'application/json'}, 
              json={'name': 'Бульбазавр','photo': 'https://dolnikov.ru/pokemons/albums/010.png'})

print(add_pokemon.text)

change_name = requests.put('https://pokemonbattle.me:9104/pokemons', 
              headers ={'trainer_token':token, 'Content-Type':'application/json'}, 
              json={'pokemon_id': 7218, 'name': 'Бульбазавр_new','photo': 'https://dolnikov.ru/pokemons/albums/010.png'})

print(change_name.text)

add_pokeball = requests.post('https://pokemonbattle.me:9104/trainers/add_pokeball', 
              headers ={'trainer_token':token, 'Content-Type':'application/json'},
              json={'pokemon_id': 7218})

print(add_pokeball.text)







