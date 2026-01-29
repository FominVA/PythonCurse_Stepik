import json


with open('food_services.json', encoding='utf-8') as file:
    data = json.load(file)

largest = {}

for place in data:
    type_obj = place['TypeObject']
    seats = place['SeatsCount']

    if type_obj not in largest or seats > largest[type_obj][1]:
        largest[type_obj] = (place['Name'], seats)

for type_obj, (name, seats) in sorted(largest.items()):
    print(f'{type_obj}: {name}, {seats}')