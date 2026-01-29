from datetime import date, datetime, timedelta, time
pattern = '%d.%m.%Y %H:%M'
d = datetime.strptime(input(), pattern)
td = timedelta(hours=d.hour, minutes=d.minute)


if d.weekday() < 5 and timedelta(hours=9) <= td < timedelta(hours=21):
    print(int((timedelta(hours=21)-td).total_seconds() // 60))
elif d.weekday() > 4 and timedelta(hours=10) <= td < timedelta(hours=18):
    print(int((timedelta(hours=18)-td).total_seconds()//60))
else:
    print('Магазин не работает')   

