import csv

with open('sales.csv', 'r', encoding='utf-8', newline='') as file:
    header = file.readline()
    rows = csv.reader(file, delimiter=';')
    
    for row in rows:
        name = row[0]
        old_price = int(row[1])
        new_price = int(row[2])
        if old_price > new_price:
            print(name)
            
    