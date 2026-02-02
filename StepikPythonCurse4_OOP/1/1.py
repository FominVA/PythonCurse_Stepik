from datetime import datetime, timedelta

# Получаем текущую дату и время
today = datetime.now()

# Создаем объект timedelta с разницей в 42 дня
delta = timedelta(days=42)

# Вычисляем новую дату
future_date = today + delta

print(f"Сегодня: {today.strftime('%d.%m.%Y')}")
print(f"Через 42 дня: {future_date.strftime('%d.%m.%Y')}")