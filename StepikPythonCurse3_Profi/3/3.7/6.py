from datetime import datetime, date
import calendar

def get_days_in_month(year, month):
    l = list(calendar.month_name)
    m = l.index(month)
    s = calendar.monthrange(year, m)
    result = [date(year, m, i) for i in range(1, s[1]+1)]
    print(sorted(result))
    



get_days_in_month(2021, 'December')