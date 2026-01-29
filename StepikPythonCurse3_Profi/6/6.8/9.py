from collections import Counter

def print_bar_chart(data, mark):
    result = Counter(data)
    max_len = max(map(len, result.keys()))
    for word, count in result.most_common():
        print(f'{word:<{max_len}} |{count*mark}')

print_bar_chart('beegeek', '+')
