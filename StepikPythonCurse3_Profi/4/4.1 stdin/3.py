import sys
from datetime import datetime

data = list(map(str.strip, sys.stdin))
if len(data)%2 ==0 and int(data[-1])%2 ==0:
    print('Дима')  
elif len(data)%2 !=0 and int(data[-1])%2!=0:
    print('Дима')
elif len(data)%2 ==0 and int(data[-1])%2!=0:
    print('Анри')    
elif len(data)%2 !=0 and int(data[-1])%2 ==0:
    print('Анри')