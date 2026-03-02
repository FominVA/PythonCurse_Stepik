class Queue:

    def __init__(self, *args):
        self.parts = list(args)
        
    def add(self, *args):
        return self.parts.extend(args)

    def pop(self):
        # Проверяем, не пуста ли очередь
        if not self.parts:
            return None
        # В очереди (FIFO) первым выходит тот, кто зашел первым (индекс 0)
        return self.parts.pop(0)

    def __str__(self):
        return ' -> '.join(map(str, self.parts))

    def __eq__(self, other):
        # Проверяем, является ли другой объект экземпляром класса Queue
        if not isinstance(other, Queue):
            return False
        # Сравниваем внутренние списки элементов
        return self.parts == other.parts
    
    def __add__(self, other):
        if isinstance(other, Queue):
            new_elements = self.parts + other.parts
            return Queue(*new_elements)
        return NotImplemented
    
    def __iadd__(self, other):
        if isinstance(other, Queue):
            # Расширяем текущий список элементов
            self.parts.extend(other.parts)
            # Возвращаем self, чтобы сохранить id
            return self
        return NotImplemented

    def __rshift__(self, n):
        if isinstance(n, int):
            new_elements = self.parts[n:]
            return Queue(*new_elements)
        return NotImplemented

queue = Queue(1, 2, 3, 4, 5)

print(queue >> 3)