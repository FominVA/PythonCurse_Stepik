import calendar

s = input().split(' ')
l = list(calendar.month_name)
m = l.index(s[1])

print((calendar.monthrange(int(s[0]), m))[1])