from datetime import datetime, date, timedelta

d = input()
day = timedelta(days=1)
my_date = datetime.strptime(d, '%d.%m.%Y')
dt1 = (my_date-day).strftime('%d.%m.%Y')
dt2 = (my_date+day).strftime('%d.%m.%Y')
print(dt1, dt2, sep='\n')