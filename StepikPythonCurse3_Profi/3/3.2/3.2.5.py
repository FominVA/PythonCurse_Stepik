from datetime import date

dates = [date.fromisoformat(input()) for i in range(2)]
print((min(dates)).strftime('%d-%m (%Y)'))