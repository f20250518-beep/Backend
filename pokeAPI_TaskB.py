import requests
import json
import pandas
import os

info = [['']]
i = 1
typeID = []
response = requests.get("https://pokeapi.co/api/v2/type/")
types = response.json()
count = types['count']

for a in types['results']:
    typeID.append(a['url'].split('/')[-2])
    info[0].append(a['name'])
    info.append([a['name']])
    x=1
    while x<count:
        info[len(info)-1].append('1')
        x += 1

while i<count:
    response = requests.get("https://pokeapi.co/api/v2/type/" + typeID[i-1])
    types = response.json()
    nameDD = [a['name'] for a in types['damage_relations']['double_damage_from']]
    j = 0
    length = len(nameDD)
    while j<length:
        info[i][info[0].index(nameDD[j])] = '2'
        j += 1
    nameHD = [a['name'] for a in types['damage_relations']['half_damage_from']]
    j = 0
    length = len(nameHD)
    while j<length:
        info[i][info[0].index(nameHD[j])] = '0.5'
        j += 1
    nameND = [a['name'] for a in types['damage_relations']['no_damage_from']]
    j = 0
    length = len(nameND)
    while j<length:
        info[i][info[0].index(nameND[j])] = '0'
        j += 1
    i += 1


table = pandas.DataFrame(info[1:], columns=info[0])
table.to_csv("damageMatrix.csv", index=False)



