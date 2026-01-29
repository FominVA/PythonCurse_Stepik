import json

with open('data.json', 'r', encoding='utf-8') as file, open('updated_data.json', 'w', encoding='utf-8') as file2:
    result = []
    data = json.load(file)
    for item in data:
        if type(item) == str:
            result.append(item+'!')
        elif type(item)==int:
            result.append(item+1)
        elif type(item)==bool:
            if item==False:
                result.append(True)
            else:
                result.append(False)
        elif type(item)==list:
            result.append(item*2)
        elif type(item)==dict:
            item.update({"newkey": None})
            result.append(item)
    
    json.dump(result, file2)
    