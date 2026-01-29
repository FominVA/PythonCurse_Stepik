import json
with open('people.json', 'r', encoding='utf-8') as file1:
    data = json.load(file1)
    pattern = max(data, key=len)
    for people in data:
        for i in pattern:
            people[i] = people.get(i, None)
            
            
with open('updated_people.json', 'w', encoding='utf-8') as file2:
    json.dump(data, file2)