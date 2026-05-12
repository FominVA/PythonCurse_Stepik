class ReadableTextFile:

    def __init__(self, filename):
        self.filename = filename


    def __enter__(self):
        self.file = open(self.filename, 'r', encoding="UTF-8")
        return (line.strip() for line in self.file)

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()



with open('glados_quotes.txt', 'w', encoding='utf-8') as file:
    print('Только посмотрите!', file=file)
    print('Как величаво она парит в воздухе', file=file)
    print('Как орел', file=file)
    print('На воздушном шаре', file=file)

with ReadableTextFile('glados_quotes.txt') as file:
    for line in file:
        print(line)