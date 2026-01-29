from datetime import datetime, time, timedelta
pattern = '%H:%M'

start = datetime.strptime(input(), pattern)
end = datetime.strptime(input(), pattern)

while (start + timedelta(minutes=45)) <= end:
    print(start.strftime(pattern), '-', (start+timedelta(minutes=45)).strftime(pattern))
    start += timedelta(minutes=55)





# 10:00
# 12:35