from itertools import groupby


def group_anagrams(words):
    sorted_words = sorted(words, key=sorted)
    groups = groupby(sorted_words, key=sorted)
    return [tuple(group) for _, group in groups]


groups = group_anagrams(['evil', 'father', 'live', 'levi', 'book', 'afther', 'boko'])

print(*groups)