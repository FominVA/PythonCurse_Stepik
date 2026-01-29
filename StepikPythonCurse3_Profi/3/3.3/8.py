from datetime import datetime, timedelta
def fill_up_missing_dates(dates):
    datetime_dates = [datetime.strptime(d, '%d.%m.%Y') for d in dates]
    min_date = (min(datetime_dates)).toordinal()
    max_date = (max(datetime_dates)).toordinal()
    new_dates = []
    for i in range(min_date, max_date+1):
        d = datetime.fromordinal(i)
        d = datetime.strftime(d, '%d.%m.%Y')
        new_dates.append(d)
    return new_dates



dates = ['01.11.2021', '07.11.2021', '04.11.2021', '03.11.2021']

print(fill_up_missing_dates(dates))