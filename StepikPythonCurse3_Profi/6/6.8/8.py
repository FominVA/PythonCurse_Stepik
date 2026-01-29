from collections import Counter

def scrabble(symbols, word):
    data_s = Counter(symbols.lower())
    data_w = Counter(word.lower())
    return data_s >= data_w





print(scrabble('bbbbbeeeeegggggggeeeeeekkkkk', 'Beegeek'))