from datetime import datetime
pattern = '%d.%m.%Y'

n = int(input())
names = {}
for i in range(n):
    name, birth = input().rsplit(' ', 1)
    birth = datetime.strptime(birth, pattern)
    names[birth] = names.setdefault(birth, [])+[name]

max_value = 0
for value in names.values():
    if len(value) > max_value:
        max_value = len(value)

result = []
for key, value in names.items():
    if len(value) == max_value:
        result.append(key)

result=sorted(result)
for i in result:
    print(datetime.strftime(i, pattern))

