import csv
from datetime import datetime
columns=['username','email','dtime']

with open('name_log.csv', encoding='utf-8', newline='') as file1, open ('new_name_log.csv','w',encoding='utf-8',newline='') as file2:
    reader = csv.DictReader(file1, delimiter=',')
    
    sorted_data= sorted(reader, key=lambda x: datetime.strptime(x['dtime'], '%d/%m/%Y %H:%M'))
    result = sorted(sorted_data, key=lambda x: x['email'])
    
    writer = csv.DictWriter(file2, fieldnames=columns)
    writer.writeheader()
    for row in result:
        writer.writerow(row)
