from datetime import datetime
with open('diary.txt') as file:
    rows = file.read().split("\n\n")
    rows = sorted(rows, key=lambda x: datetime.strptime(x.split('\n')[0], '%d.%m.%Y; %H:%M'))
    for i in rows:
        print(i, end = "\n")
        print()