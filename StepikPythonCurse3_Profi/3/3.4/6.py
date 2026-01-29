from datetime import date, time, datetime, timedelta


def num_of_sundays(year):
    y = datetime(year, 12, 31)
    return y.strftime('%U')

print(num_of_sundays(2021))