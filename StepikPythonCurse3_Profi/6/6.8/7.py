from collections import Counter
import csv

with open('./6/6.8/name_log.csv', 'r', encoding='utf-8') as file:
    rows = list(csv.reader(file))
    columns=['username','email','dtime']
    rows = rows[1:]
    result = []
    for row in rows:
        row = row[1]
        result.append(row)
    sorted_result = Counter(sorted(result, key=lambda x: x[0]))
    
    for email, count in sorted(sorted_result.items()):
        print(f'{email}: {count}')



  