import json
import csv

with open('playgrounds.csv', 'r', encoding='utf-8') as file1, open('addresses.json', 'w', encoding='utf-8') as file2:
    reader = csv.DictReader(file1, delimiter=';')
    
    result = {}
    for row in reader:
        result.setdefault(row['AdmArea'], {}).setdefault(row['District'], []).append(row['Address'])

    json.dump(result, file2, indent=3, ensure_ascii=False)