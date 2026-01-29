from datetime import datetime, timedelta
pattern = '%d.%m.%Y'
nearest_date = datetime.strptime(input(), pattern)
n = int(input())
names = {}
for i in range(n):
    name, birth = input().rsplit(' ', 1)
    birth = datetime.strptime(birth, pattern)
    names[birth] = names.setdefault(birth, [])+[name]
result = []
for keys, values in names.items():
    if nearest_date < keys.replace(year=nearest_date.year) <= (nearest_date+timedelta(days=7)):
        result.append(keys)


if len(result) != 0:
    print(*names.get(max(result)))
else:
    print('Дни рождения не планируются')

        


