from sympy import isprime 

def primes(left, right):
    for num in range(left, right+1):
        if isprime(num):
            yield num


generator = primes(1, 15)

print(*generator)