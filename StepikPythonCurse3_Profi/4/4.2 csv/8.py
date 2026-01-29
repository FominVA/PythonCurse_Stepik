import csv

with open('titanic.csv', encoding='utf-8', newline='') as file:
    reader = list(csv.reader(file, delimiter=';'))
    
    female = []
    male = []
    for row in reader[1:]:
        if int(row[0]) == 1 and row[2]=='female' and float(row[3]) < 18:
            female.append(row[1])
        elif int(row[0]) == 1 and row[2]=='male' and float(row[3]) < 18:
            male.append(row[1])
    print(*male, sep='\n')
    print(*female, sep='\n')
         


# import csv

# with open('titanic.csv', encoding='utf-8', newline='') as file:
#     reader = csv.DictReader(file, delimiter=";")
#     passangers = list(filter(lambda x: x['survived']=='1' and float(x['age'])<18, reader))
#     passangers = sorted(passangers, key=lambda x: x['sex'], reverse=True)
#     for row in passangers:
#         print(row['name'])