from datetime import datetime, date, time, timedelta

t = datetime.strptime(input(), '%H:%M:%S')
s = timedelta(seconds = int(input()))
result = t+s
print(result.strftime('%H:%M:%S'))

