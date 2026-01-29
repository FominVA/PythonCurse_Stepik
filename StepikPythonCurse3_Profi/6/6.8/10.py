from collections import defaultdict
import csv
import json

d = defaultdict(int)
for num in range(1, 5):
    with open(f'./6/6.8/quarter{num}.csv', 'r', encoding='utf-8') as quarter:
        rows = list(csv.reader(quarter))[1:]
        for i in rows:
            d[i[0]]+= int(i[1])+int(i[2])+int(i[3])

with open ('./6/6.8/prices.json',encoding='UTF-8') as data:
    prices = json.load(data)

result = 0

for name, count in d.items():
    result += prices[name]*count
    
print(result)

     
