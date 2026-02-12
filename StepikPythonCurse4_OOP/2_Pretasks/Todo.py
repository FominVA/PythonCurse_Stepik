class Todo:
    def __init__(self):
        self.things = []

    def add(self, task, priority):
        self.things.append((task, priority))
                  
    def get_by_priority(self, n): #метод, принимающий в качестве аргумента целое число n и возвращающий список названий дел, имеющих приоритет n
        result = []
        for tup in self.things:
            if tup[1] == n:
                result.append(tup[0])
        return result
    

    def get_low_priority(self): #метод, возвращающий список названий дел, имеющих самый низкий приоритет 
        low_priority = min(map(lambda t: t[1], self.things)) if self.things else None
        return self.get_by_priority(low_priority)
    
    def get_high_priority(self): #метод, возвращающий список названий дел, имеющих самый высокий приоритет 
        high_priority = max(map(lambda t: t[1], self.things)) if self.things else None
        return self.get_by_priority(high_priority)
