def limited_hash(left, right, hash_function=hash):
    length = right-left+1
    def wrapper(obj):
        hash_val = hash_function(obj)
        if hash_val in range(left, right):
            return hash_val
        return left + (hash_val - left) % length
    return wrapper

hash_function = limited_hash(2, 3, hash_function=lambda obj: len(str(obj)))

print(hash_function('a'))
print(hash_function('ab'))
print(hash_function('abc'))
print(hash_function('abcd'))
print(hash_function('abcde'))
print(hash_function('abcdef'))
print(hash_function('abcdefg'))