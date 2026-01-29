import csv
import json
from datetime import datetime 
with open('pools.json', 'r', encoding='utf-8') as file1:
    data = json.load(file1)
    result = []
    open = datetime.strptime('10:00', '%H:%M')
    close = datetime.strptime('12:00', '%H:%M')
    for row in data:
        work_time = (row['WorkingHoursSummer']['Понедельник']).split('-')
        if open<= datetime.strptime(work_time[0], '%H:%M') < close and open < datetime.strptime(work_time[1], '%H:%M') >= close:
            result.append((row["Address"], row["DimensionsSummer"]["Length"], row["DimensionsSummer"]["Width"], row["DimensionsSummer"]["Square"]))
    result = list(sorted(result, key=lambda x: x[3], reverse=True))
    print(result[0][1],'x',result[0][2], sep='')
    print(result[0][0])