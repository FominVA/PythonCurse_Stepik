from datetime import date, datetime, timedelta
import calendar

def get_all_mondays(year):
    result = []
    current_date = datetime(year, 1, 1)
    while current_date.year == year:
        if current_date.weekday() == 0:
            result.append(current_date.date())
        current_date += timedelta(days=1)
    return result

get_all_mondays(2021)