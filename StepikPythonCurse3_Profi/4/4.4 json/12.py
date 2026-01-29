import csv
import json

with open('students.json', 'r', encoding='utf-8') as file1, open('data1.csv', 'w', encoding='utf-8', newline='') as file2:
    students = json.load(file1)
    headers = ['name', 'phone']
    data = []
    for row in students:
        if row['age'] >= 18 and row['progress'] >= 75:
            data.append([row['name'], row['phone']])
    data = sorted(data)
    writer = csv.writer(file2)
    writer.writerow(headers)

    for row in data:
        writer.writerow(row)
