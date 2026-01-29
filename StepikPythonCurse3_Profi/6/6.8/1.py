from collections import Counter

s = input().lower().split(' ')

berry = Counter(s)
print(berry.most_common(1)[0][0])