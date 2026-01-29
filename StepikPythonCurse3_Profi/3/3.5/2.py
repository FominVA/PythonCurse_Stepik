from datetime import datetime, timedelta
import time
print(f"Здесь мы начинаем перебирать ежемесячно...")
t = time.perf_counter()
pattern = '%d.%m.%Y'

start = datetime.strptime('01.01.0001', pattern)
end = datetime.strptime('31.12.9999', pattern)

def bad_day(num):
    count=0
    for j in range(start.toordinal(), end.toordinal()+1):
        if datetime.fromordinal(j).day == 13 and datetime.fromordinal(j).weekday() == num:
            count += 1
    print(count)

for num in range(7):
    bad_day(num)

print(f"Более разумный перебор:  {time.perf_counter() - t} с.")