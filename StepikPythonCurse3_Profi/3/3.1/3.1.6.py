from datetime import date

def get_date_range(start, end):
    return [date.fromordinal(i) for i in range(start.toordinal(), end.toordinal() + 1)]



date1 = date(2021, 10, 1)
date2 = date(2021, 10, 5)

print(*get_date_range(date1, date2), sep='\n')