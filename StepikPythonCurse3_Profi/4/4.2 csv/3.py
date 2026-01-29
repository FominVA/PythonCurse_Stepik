import csv

salaries = {}

with open('salary_data.csv', encoding='utf-8') as file:
    reader = csv.reader(file, delimiter=';')
    next(reader)
    for company, salary in reader:
        if company not in salaries:
            salaries[company] = [0, 0]
        salaries[company][0] += int(salary)
        salaries[company][1] += 1

sorted_companies = sorted(salaries, key=lambda c: (salaries[c][0] / salaries[c][1], c))
print(*sorted_companies, sep='\n')