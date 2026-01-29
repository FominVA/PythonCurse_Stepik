from datetime import date, datetime, timedelta
import calendar

def get_all_days(year):
    result = []
    current_date = datetime(year, 1, 1)
    while current_date.year == year:
        if current_date.weekday() == 3 and 15 <= current_date.day <=21:
            result.append(datetime.strftime(current_date, '%d.%m.%Y'))
        current_date += timedelta(days=1)
    print(*result, sep='\n')

get_all_days(int(input()))