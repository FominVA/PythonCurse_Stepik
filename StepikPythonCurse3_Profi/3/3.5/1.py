from datetime import date, time, datetime, timedelta
from functools import reduce
import operator
pattern = '%H:%M'
data = [('07:14', '08:46'),
        ('09:01', '09:37'),
        ('10:00', '11:43'),
        ('12:13', '13:49'),
        ('15:00', '15:19'),
        ('15:58', '17:24'),
        ('17:57', '19:21'),
        ('19:30', '19:59')]
total = []
for t in data:
    s = datetime.strptime(t[1], pattern) - datetime.strptime(t[0], pattern)
    total.append(s)
time_1 = reduce(operator.add, total)
time_obj = datetime.strptime(str(time_1), '%H:%M:%S')  
result = time_obj.hour * 60 + time_obj.minute 
print(result)