import sys
from datetime import datetime

data = list(map(str.strip, sys.stdin))
   
new_data = []
for i in data:
    a = datetime.strptime(i, '%d.%m.%Y')
    new_data.append(a)
ASC = sorted(new_data)
DESC = sorted(new_data, reverse =True)

if new_data == ASC and len(new_data) == len(set(new_data)):
    print('ASC')
elif new_data == DESC and len(new_data) == len(set(new_data)):
    print('DESC')
else:
    print('MIX')