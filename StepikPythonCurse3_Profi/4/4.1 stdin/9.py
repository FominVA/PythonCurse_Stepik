import sys
import math
data = list(map(str.strip, sys.stdin))
sort_data = sorted(data)

if (int(data[0])+int(data[2]))/2 == int(data[1]) and len(data) == len(set(sort_data)):
    print('Арифметическая прогрессия')
elif math.sqrt(int(data[0])*int(data[2])) == int(data[1]) and math.sqrt(int(data[-1])*int(data[-3])) == int(data[-2]) and len(data) == len(set(sort_data)):
    print('Геометрическая прогрессия')
else:
    print('Не прогрессия')
