from collections import Counter

s = Counter(sorted(input().split(',')))
length = []
for i in s:
    length.append(len(i))
    
for product, count in s.items():
    uc = 0
    for i in product.replace(' ',''):
        uc += ord(i)

    print(f'{product.ljust(max(length))}: {uc} UC x {count} = {uc*count} UC')

