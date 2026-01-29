import json
import csv
from datetime import datetime

with open('exam_results.csv','r',encoding='UTF-8') as file1, open ('best_scores.json','w',encoding='UTF-8') as file2:
    data = list(csv.reader(file1))
    d= []
    d2 =[]
    for persona in data[1:]:
        d.append({'name': persona[0], 'surname': persona[1], 'best_score': int(persona[2]),
                  'date_and_time': datetime.strptime(persona[3], '%Y-%m-%d %H:%M:%S'), 'email': persona[4]})
    result = sorted(d,key=lambda x:(x['email'],x['best_score'],x['date_and_time']),reverse=True)
    d2.append(result[0])
    d2[0]['date_and_time']=d2[0]['date_and_time'].strftime('%Y-%m-%d %H:%M:%S')
    for i in range(1,len(result)):
        if result[i]['email'] != result[i-1]['email']:
            result[i]['date_and_time']=(result[i].get('date_and_time')).strftime('%Y-%m-%d %H:%M:%S')
            d2.append(result[i])
    json.dump(sorted(d2,key=lambda x:x['email']), file2,indent=3)
