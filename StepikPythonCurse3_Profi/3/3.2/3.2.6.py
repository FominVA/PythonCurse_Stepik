from datetime import date
n = int(input())
dates = [date.fromisoformat(input()) for i in range(n)]
dates = sorted(dates)
dates = [i.strftime('%d/%m/%Y') for i in dates]
print(*dates, sep='\n')