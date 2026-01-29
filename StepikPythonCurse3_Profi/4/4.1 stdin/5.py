import sys

data = list(map(str.strip, sys.stdin))
count = 0
for i in data:
    if i.startswith('#') == True:
        count += 1
print(count)