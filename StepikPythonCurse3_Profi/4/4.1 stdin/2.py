import sys
from datetime import datetime

data = list(map(str.strip, sys.stdin))
new_data = []
for i in data:
    s = datetime.strptime(i, '%Y-%m-%d')
    new_data.append(s.toordinal())
result = max(new_data) - min(new_data)
print(result)
