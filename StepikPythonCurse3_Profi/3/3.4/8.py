from datetime import datetime, date, timedelta

datas = [datetime.strptime(i, '%d.%m.%Y') for i in input().split(' ')]
l = []
for d in range(1, len(datas)):
    if len(datas) <= 1:
        print([])
    else:
        day_count = abs((datas[d]-datas[d-1]).days)
        l.append(day_count)
print(l)