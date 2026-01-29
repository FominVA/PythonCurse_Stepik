import csv

s = int(input()) - 1

with open('deniro.csv', 'w') as file:
    reader = csv.reader(file, delimiter=',')
    new_reader = sorted(reader, key=lambda x: int(x[s]) if x[s].isdigit() else x[s])   
    for row in new_reader:
        print(*row, sep=',')
    