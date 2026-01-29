import calendar
l = [int(i) for i in input().split(' ')]
s = calendar.monthrange(l[0], l[1])
print(s[1])