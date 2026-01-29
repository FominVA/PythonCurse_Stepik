import csv
from collections import Counter

columns = ['domain', 'count']
domains = []
with open('data.csv', encoding='utf-8') as file:
    rows = csv.reader(file,delimiter=',')
    next(rows)
    for first_name, surname, email in rows:
        r = email.split('@')[1]
        domains.append(r)
    
    domain_counts = Counter(domains)
    sorted_domains = sorted(domain_counts.items(), key=lambda item: (item[1], item[0]))
    

    with open('domain_usage.csv', 'w', encoding='utf-8', newline='') as file1:
         writer = csv.writer(file1)
         writer.writerow(columns)
         for row in sorted_domains:                         # запись строк
             writer.writerow(row)  