from datetime import date

while True:
    try:
        day, month, year = input().split('.')
        my_date = date(int(year), int(month), int(day))
        print('Корректная')
    except ValueError:
        break