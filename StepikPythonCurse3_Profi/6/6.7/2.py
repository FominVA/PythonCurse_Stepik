from collections import Counter

def count_occurences(word, words):
    result = Counter(words.lower().split(' '))
    return result[word.lower()]


word = 'python'
words = 'Python Conferences python training python events'

print(count_occurences(word, words))