def is_iterator(obj):
    try:
        if next(obj):
            return True
    except:
        return False
    

print(is_iterator([1, 2, 3, 4, 5]))