from math import factorial                   # функция из модуля math     
import time

def for_and_append(iterable):             # с использованием цикла for и метода append()
    result = []
    for elem in iterable:
        result.append(elem)
    return result
        

def list_comprehension(iterable):         # с использованием списочного выражения
    return [elem for elem in iterable]    
    

def list_function(iterable):              # с использованием встроенной функции list()
    return list(iterable) 


for func in (for_and_append, list_comprehension, list_function):
    start = time.perf_counter()
    func('100_000')
    end = time.perf_counter()
    t = end - start
    print(t)