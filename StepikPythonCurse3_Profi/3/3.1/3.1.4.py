from datetime import date

dates = [date(2010, 9, 28), date(2017, 1, 13), date(2009, 12, 25), date(2010, 2, 27), date(2021, 10, 11), date(2020, 3, 13), date(2000, 7, 7), date(1999, 4, 14), date(1789, 11, 19), date(2013, 8, 21), date(1666, 6, 6), date(1968, 5, 26)]

for date in dates:
    if date.month < 4:
        print(f'{date.year}-Q1')
    elif date.month < 7:
        print(f'{date.year}-Q2')
    elif date.month < 10:
        print(f'{date.year}-Q3')
    else:
        print(f'{date.year}-Q4')