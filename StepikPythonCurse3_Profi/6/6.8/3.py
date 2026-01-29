from collections import Counter

berry = Counter(input().lower().split(' '))

s = sorted([key for key, value in berry.items() if value >= berry.most_common()[0][1]], reverse=True)

print(s[0])