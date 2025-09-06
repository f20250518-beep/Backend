import requests
import json
import pandas

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
        info[i][info[0].index(nameDD[j])] = '   2'
        j += 1
    nameHD = [a['name'] for a in types['damage_relations']['half_damage_from']]
    j = 0
    length = len(nameHD)
    while j<length:
        info[i][info[0].index(nameHD[j])] = '   0.5'
        j += 1
    nameND = [a['name'] for a in types['damage_relations']['no_damage_from']]
    j = 0
    length = len(nameND)
    while j<length:
        info[i][info[0].index(nameND[j])] = '   0'
        j += 1
    i += 1


p = 0
while p == 0:
    endpoint = input("Enter Endpoint In Proper Format: \n")
    if endpoint == "q":
        break
    endpoint = endpoint.split()[-1]
    baseUrl = endpoint.split('?')[-2]
    subEndpoint = endpoint.split('?')[-1]
    subSubEndpoint = subEndpoint.split('&')
    side = []
    sideType = []
    allInfo = []
    for b in subSubEndpoint:
        side.append((b.split('=')[-2]).lower())
        sideType.append((b.split('=')[-1]).lower())
    if len(side) == 1:
        index = info[0].index(sideType[0])
        if side[0] == "defender" or side[0] == 'defender':
            i = 1
            print(f"defender : {info[index][0]} \n")
            while i<21:
                allInfo.append(f"{info[0][i]} : {info[index][i]}")
                i += 1
        elif side[0] == "attacker" or side[0] == 'attacker':
            i = 1
            print(f"defender : {info[0][index]} \n")
            while i<21:
                allInfo.append(f"{info[i][0]} : {info[i][index]}")
                i += 1
    else:
        for d in info:
            row = d.index(sideType[side.index("defender" or 'defender')])
            if row != -1:
                break
        col = info[0].index(sideType[side.index("attacker" or 'attacker')])
        allInfo = [f"defender : {info[row][0]}", f"attacker : {info[0][col]}", f"multiplier : {info[row][col]}"]
    for c in allInfo:
        print(c, "\n")

table = pandas.DataFrame(info[1:], columns=info[0])
table.to_csv("damageMatrix.csv", index=False)
