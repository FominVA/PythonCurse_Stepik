class CachedFunction:

    def __init__(self, func):
        self.cache = {}
        self.func = func

    def __call__(self, *args):
        if args in self.cache:
            return self.cache[args]
        else:
            result = self.func(*args)
            self.cache[args] = result
            return result
        
@CachedFunction
def slow_fibonacci(n):
    if n == 1:
        return 0
    elif n in (2, 3):
        return 1
    return slow_fibonacci(n - 1) + slow_fibonacci(n - 2)
    
slow_fibonacci(5)

for args, value in sorted(slow_fibonacci.cache.items()):
    print(args, value)