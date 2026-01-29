from datetime import datetime, timedelta
import time


t = time.perf_counter()

print("Мы здесь перебираем все даты...")
d = datetime(1, 1, 1)
weekdays = {}
while d < datetime(9999, 12, 31):
    if d.day == 13:
        weekdays[d.weekday()] = weekdays.get(d.weekday(), 0) + 1
    d += timedelta(1)

print(f"Обычный перебор:         {time.perf_counter() - t} с.\n")
del t, weekdays, d

print(f"Здесь мы начинаем перебирать ежемесячно...")
t = time.perf_counter()
d = datetime(1, 1, 1)
weekdays = {}
while d < datetime(9999, 12, 31):
    if d.day == 13:
        weekdays[d.weekday()] = weekdays.get(d.weekday(), 0) + 1
        if d < datetime(9999, 12, 31) - timedelta(28):
            d += timedelta(27)
    d += timedelta(1)

print(f"Более разумный перебор:  {time.perf_counter() - t} с.")