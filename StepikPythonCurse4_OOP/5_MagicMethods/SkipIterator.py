class SkipIterator:
    def __init__(self, iterable, n):
        self.iterator = iter(iterable)
        self.n = n

    def __iter__(self):
        return self

    def __next__(self):
        # Получаем очередной элемент, который нужно вернуть
        item = next(self.iterator)

        # Пытаемся пропустить n элементов
        for _ in range(self.n):
            try:
                next(self.iterator)
            except StopIteration:
                # Если элементы закончились во время пропуска — просто прекращаем пропускать
                break

        return item

skipiterator = SkipIterator([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 0)   # пропускаем по одному элементу

print(*skipiterator)