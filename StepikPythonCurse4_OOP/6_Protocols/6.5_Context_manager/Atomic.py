import copy
from typing import Any, Union, List, Set, Dict

class Atomic:

    def __init__(self, data: Union[List, Set, Dict], deep: bool = False):
        self.data = data
        self.deep = deep
        self.copy = None

    def __enter__(self) -> Union[List, Set, Dict]:
        if self.deep:
            self.copy = copy.deepcopy(self.data)
        else:
            if isinstance(self.data, list):
                self.copy = self.data[:]
            elif isinstance(self.data, set):
                self.copy = set(self.data)
            elif isinstance(self.data, dict):
                self.copy = dict(self.data)
            else:
                raise TypeError
        return self.copy

    def __exit__(self, exc_type, exc_val, exc_tb) -> bool:
        if exc_type is None:
            if isinstance(self.data, list):
                self.data.clear()
                self.data.extend(self.copy)
            elif isinstance(self.data, set):
                self.data.clear()
                self.data.update(self.copy)
            elif isinstance(self.data, dict):
                self.data.clear()
                self.data.update(self.copy)
        else:
            return self.data
        return False

matrix = [[1, 2], [3, 4]]

with Atomic(matrix, True) as atomic:
    atomic[1].append(0)       # изменение вложенной структуры
    atomic.append([5, 6])
    del atomic[100]           # обращение по несуществующему индексу

print(matrix)