from itertools import dropwhile

def drop_this(iterable, obj):
    i = dropwhile(lambda x: x != obj, iterable)
    return i