from collections import Counter

berry = Counter(input().lower().split(' '))

s = sorted([key for key, value in berry.items() if value <= berry.most_common()[-1][1]])

print(', '.join(s))




