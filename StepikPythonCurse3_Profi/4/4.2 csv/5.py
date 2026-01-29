import csv

#def csv_columns(filename):
with open('deniro.csv', encoding='utf-8') as file:
    rows = list(csv.reader(file, delimiter=','))
    d={}
    keys = rows[0]
    for row in rows[1:]:
        for i in range(len(row)):
            d.setdefault(keys[i], []).append(row[i])
    print(d)
    #return d
#csv_columns('deniro.csv')