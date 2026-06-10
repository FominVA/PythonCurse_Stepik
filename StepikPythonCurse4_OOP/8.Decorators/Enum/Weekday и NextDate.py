from enum import Enum
from datetime import datetime, timedelta

class Weekday(Enum):
    MONDAY=0
    TUESDAY=1
    WEDNESDAY=2
    THURSDAY=3
    FRIDAY=4
    SATURDAY=5
    SUNDAY=6

class NextDate:
    def __init__(self, today, weekday, considering_today=False):
        self.today = today
        self.weekday = weekday
        self.considering_today = considering_today

    def date(self):
        days_ahead = (self.weekday.value - self.today.weekday()) % 7
        if days_ahead == 0 and not self.considering_today:
            days_ahead = 7
        return self.today + timedelta(days=days_ahead)

    def days_until(self):
        days_ahead = (self.weekday.value - self.today.weekday()) % 7
        if days_ahead == 0 and not self.considering_today:
            days_ahead = 7
        return days_ahead



from datetime import date

today = date(2023, 4, 17)                              # понедельник
next_friday = NextDate(today, Weekday.FRIDAY)          # следующая пятница

print(next_friday.date())
print(next_friday.days_until())