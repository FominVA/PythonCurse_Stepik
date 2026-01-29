import json
from zipfile import ZipFile

def is_correct_json(string):
    try:
        json.loads(string)
        return True
    except:
        return False
    
with ZipFile('data.zip', mode='r') as zip_file:
    players = []
    for i in zip_file.infolist():
        if not i.is_dir() and i.filename.endswith('.json'):
            with zip_file.open(i.filename, 'r') as j_file:
                content = j_file.read()
                
                if is_correct_json(content):
                    data = json.loads(content)
                    if isinstance(data, dict) and data.get('team') == 'Arsenal':
                        players.append((data.get('first_name'), data.get('last_name')))
    players.sort()
    for first_name, last_name in players:
        print(f'{first_name} {last_name}')
                        