cache = {1:2, 2: 2}
def fibonachi(n):
    result = cache.get(n)
    if result is None:
        result = fibonachi(n-2) + fibonachi(n-1)
    cache[n] = result
    return result

print(fibonachi(4))
