from datetime import date

def print_good_dates(dates):
    dates = sorted(dates)
    for d in dates:
        if int(d.strftime('%Y'))==1992 and (int(d.strftime('%d'))+int(d.strftime('%m'))==29):
            print(d.strftime('%B %d, %Y'))

dates = [date(1992, 10, 19), date(1991, 12, 6), date(1992, 9, 20)]
print_good_dates(dates)