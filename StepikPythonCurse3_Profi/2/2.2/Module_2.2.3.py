
n = int(input())
numbers = range(1, n+1)
d = {}

for num in numbers:
    sum_num = sum([int(digit) for digit in str(num)])
    d.setdefault(sum_num, []).append(num)
          
    
print(max(map(len, d.values())))
    