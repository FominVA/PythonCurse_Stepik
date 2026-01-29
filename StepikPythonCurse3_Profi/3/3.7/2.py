import calendar

s = input().split(' ')
m = list(calendar.month_abbr)
ind = m.index(s[1])
print(calendar.month(int(s[0]), ind))