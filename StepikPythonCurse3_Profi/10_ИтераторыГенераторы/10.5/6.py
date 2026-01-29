def palindromes():
    num = 1
    while True:
        if str(num) == str(num)[::-1]:
            yield num
        num += 1
            
        
        

generator = palindromes()

print(next(generator))
print(next(generator))
print(next(generator))
