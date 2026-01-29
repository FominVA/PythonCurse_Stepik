from datetime import datetime, timedelta
pattern = '%d.%m.%Y'
start = datetime.strptime(input(), pattern)
end = datetime.strptime(input(), pattern)

for i in range(4):
    if (start.day +start.month) % 2 ==0:
        start+=timedelta(days=1)
        
while start<=end:
    if start.weekday() not in [0,3]:
        print(start.strftime('%d.%m.%Y'))
        start+=timedelta(days=3)
    else:
        start += timedelta(days=3)
        