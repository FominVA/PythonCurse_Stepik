from contextlib import contextmanager

@contextmanager
def safe_write(filename):
    file = open(filename, 'w', encoding='UTF-8')
    try:
        yield file
    except Exception as error:
        print(f"Во время записи в файл было возбуждено исключение {type(error).__name__}")


with safe_write('undertale.txt') as file:
    file.write('Тень от руин нависает над вами, наполняя вас решительностью')

with open('undertale.txt') as file:
    print(file.read())