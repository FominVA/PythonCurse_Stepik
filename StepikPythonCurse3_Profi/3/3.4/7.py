from datetime import datetime, date, timedelta

d = datetime.strptime(input(), '%d.%m.%Y')
print(datetime.strftime(d, '%d.%m.%Y'))
for task in range(1, 10):
    day_task = task + 1
    s = timedelta(days=day_task)
    d += s
    print(datetime.strftime(d, '%d.%m.%Y'))