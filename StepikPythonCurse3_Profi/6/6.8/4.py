from collections import Counter

s = list(map(len, input().split(' ')))
len_words = Counter(s)
len_words = sorted(len_words.items(), key= lambda x: x[1])

for key, value in len_words:
    print(f'Слов длины {key}: {value}')
