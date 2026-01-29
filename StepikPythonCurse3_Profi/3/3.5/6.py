from datetime import datetime
pattern = '%d.%m.%Y'
n = int(input())
l = {}
for i in range(n):
    name, birth = input().rsplit(' ', 1)
    birthday = datetime.strptime(birth, pattern)
    l[birthday] = l.setdefault(birthday, [])+[name]

oldest = []
for key, value in l.items():
    oldest.append(datetime.toordinal(key))
max_day = datetime.fromordinal(min(oldest))
new_maxday = datetime.strptime(max_day.strftime('%d.%m.%Y'), '%d.%m.%Y')
result = l.get(new_maxday)

if len(result) == 1:
    print(new_maxday.strftime(pattern), result[0])
else:
    print(new_maxday.strftime(pattern), len(result))