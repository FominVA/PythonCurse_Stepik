class Filter:

    def __init__(self, predicate):
        self.predicate = predicate

    def __call__(self, iterable):
        result = []
        if self.predicate == None:
            for i in iterable:
                if bool(i):
                    result.append(i)
        else:            
            for i in iterable:
                if self.predicate(i):
                    result.append(i)
        return result
    
non_empty = Filter(None)

sequence = ([], False, 1, (), 'Linus Torvalds', {5, 6, 7}, True, {}, set(), '')
print(non_empty(sequence))
        