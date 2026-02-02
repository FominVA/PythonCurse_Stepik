from datetime import datetime, date
import time
import calendar

y = int(input())
m = int(input())
start = date(y, m, 1)
end = date(y, m, (calendar.monthrange(y, m))[-1])

def meetup():
    days = []
    for j in range(start.toordinal(), end.toordinal()):
        if datetime.fromordinal(j).weekday() == 3:
            days.append(datetime.fromordinal(j).day)
    meet = date(year=y, month=m, day=days[3]).strftime('%d.%m.%Y')
    return meet
    
print(meetup())
