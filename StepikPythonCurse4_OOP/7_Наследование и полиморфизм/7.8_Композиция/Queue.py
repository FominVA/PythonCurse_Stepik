class Queue:
    def __init__(self, items=None):
        self.items = []
        if isinstance(items, dict):
            for key, value in items.items():
                self.add((key, value))
        if isinstance(items, list):
            for key, value in items:
                self.add((key, value))


    def add(self, item):
        key, value = item
        for i, (k, v) in enumerate(self.items):
            if k == key:
                del self.items[i]
                break
        self.items.append((key, value))

    def pop(self):
        if self.items:
            return self.items.pop(0)
        else:
            raise KeyError('Очередь пуста')

    def __repr__(self):
        return f"Queue({self.items})"

    def __len__(self):
        return len(self.items)

queue = Queue()

try:
    queue.pop()
except KeyError as error:
    print(error)

