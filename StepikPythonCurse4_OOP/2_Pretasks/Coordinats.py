import sys

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue  
    clean_line = line.replace('(', '').replace(')', '')
    coords = [float(x) for x in clean_line.split(',')]
    print(-90<=coords[0]<=90 and -180<=coords[1]<=180)

