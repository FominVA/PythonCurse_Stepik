import calendar
from datetime import datetime
s = datetime.strptime(input(), '%Y-%m-%d').weekday()
names = list(calendar.day_name)
print(names[s])