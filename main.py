import requests
host = 'https://api.pokemonbattle.me:9104'
token = '0f9d44e19d0bf4b9d7c60113c4237d45'


response = requests.post(f'{host}/pokemons', json = {
    "name": "generate",
    "photo": "generate"
}, headers = {"Content-Type" : "application/json", "trainer_token" : token})
print(response.text)

response_name = requests.put(f'{host}/pokemons', json = {
    "pokemon_id": "22093",
    "name": "Злая Гудрон",
    "photo": "https://dolnikov.ru/pokemons/albums/087.png"
}, headers = {"Content-Type" : "application/json", "trainer_token" : token})

print(response_name.text)

response_pokeball = requests.post(f'{host}/trainers/add_pokeball', json = {
    "pokemon_id": "22094"
}, headers = {"Content-Type" : "application/json", "trainer_token" : token})

print(response_pokeball.status_code)

if response_pokeball.status_code == 200:
    print('Правильно')
else:
	print('НЕПРАВИЛЬНО!!!')
      




