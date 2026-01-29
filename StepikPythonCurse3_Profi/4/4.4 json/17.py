import json

with open('food_services.json', encoding='utf-8') as file:
    data = json.load(file)

largest ={}

for row in data:
    d_type = row['TypeObject']
    d_seats = row['SeatsCount']

    if d_type not in largest or d_seats > largest[d_type][1]:
        largest[d_type] = (row['Name'], d_seats)
    
for d_type, (name, d_seats) in sorted(largest.items()):
    print(f'{d_type}: {name}, {d_seats}')