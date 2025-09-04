import requests
import json


allInfo = {}
with open("D:\pokemon.txt") as file:
    for line in file:
        pokemon = line.strip()
        print("Getting Information For", pokemon)
        url = "https://pokeapi.co/api/v2/pokemon/" + pokemon.lower()
        response = requests.get(url)
        genData = response.json()
        url = "https://pokeapi.co/api/v2/pokemon-species/" + pokemon.lower()
        response = requests.get(url)
        speData = response.json()
        
        info ={ "Pokemon Name": genData['name'].upper(),
                "id": genData['id'],
                "abilities": [x['ability']['name'].title() for x in genData['abilities']],
                "types": [x['type']['name'].title() for x in genData['types']],
                "is_legendary": speData['is_legendary'],
                "is_mythical": speData['is_mythical']
             }

        allInfo[pokemon] = info


with open("pokeData.json", "w") as f:
        json.dump(allInfo, f, indent = 2)


