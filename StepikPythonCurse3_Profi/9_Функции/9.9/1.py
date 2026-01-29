from functools import partial

# Доступная функция (для справки)
def send_email(name, email_address, text):
    """Simulates sending an email."""
    print(f"--- Sending Email ---")
    print(f"To: {name} <{email_address}>")
    print(f"Body: {text}")
    print("-" * 20)

# 1. Реализация to_Timur()
# Фиксируем name='Тимур' и email_address='timyrik20@beegeek.ru'.
# Функция будет ожидать только 'text'.
to_Timur = partial(send_email, name='Тимур', email_address='timyrik20@beegeek.ru')

# 2. Реализация send_an_invitation()
# Фиксируем text.
# Функция будет ожидать 'name' и 'email_address'.
INVITATION_TEXT = "Школа BEEGEEK приглашает Вас на новый курс по программированию на языке Python."
send_an_invitation = partial(send_email, text=INVITATION_TEXT)


print(to_Timur('когда курс?'))