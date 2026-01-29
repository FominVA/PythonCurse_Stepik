def func(objects):
    if isinstance(objects, list):
        return objects[-1]
    elif isinstance(objects, set):
        return len(objects)
    elif isinstance(objects, tuple):
        return objects[0]
    
        

print(func(eval(input())))