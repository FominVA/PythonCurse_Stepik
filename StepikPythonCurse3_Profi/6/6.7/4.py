from collections import Counter

with open('pythonzen.txt', 'r', encoding='utf-8') as file:
    reader = file.read().lower().replace(' ','')
    result = Counter(sorted(reader))

    for letter, count in result.items():
        if letter.isalpha():
            print(f'{letter}: {count}')
    
