from datetime import datetime
def is_available_date(booked_dates, date_for_booking):
    booked =[]
    for d in booked_dates:
        if "-" in d:
            list1 = d.split('-')
            start = datetime.strptime(list1[0], '%d.%m.%Y')
            end = datetime.strptime(list1[1], '%d.%m.%Y')
            for j in range(start.toordinal(), end.toordinal()+1):
                booked.append(datetime.fromordinal(j))
        else:
            booked.append(datetime.strptime(d, '%d.%m.%Y'))

    desired = []
    if "-" in date_for_booking:
        list2 = date_for_booking.split('-')
        start = datetime.strptime(list2[0], '%d.%m.%Y')
        end = datetime.strptime(list2[1], '%d.%m.%Y')
        for j in range(start.toordinal(), end.toordinal()+1):
            desired.append(datetime.fromordinal(j))
    else:
        desired.append(datetime.strptime(date_for_booking, '%d.%m.%Y'))
    print(desired, booked)
    for dates in desired:
        if dates in booked:
            return False
            break
    return True
  


dates = ['04.11.2021', '05.11.2021-09.11.2021']
some_date = '01.11.2021-04.11.2021'
print(is_available_date(dates, some_date))