import json

with open('countries.json', 'r', encoding='utf-8') as file1, open('religion.json', 'w', encoding='utf-8') as file2:
    country = json.load(file1)
    religion = {}
    for row in country:
        religion[row["religion"]] = religion.setdefault(row["religion"], []) + [row['country']]
    
    json.dump(religion, file2, indent=3)    

    