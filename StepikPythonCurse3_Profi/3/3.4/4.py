from datetime import date, time, datetime, timedelta

t = datetime.strptime(input(),'%H:%M:%S')
result = timedelta(hours=t.hour, minutes=t.minute, seconds=t.second)
print(int(result.total_seconds()))