def filter_anagrams(word, words):
    return [i for i in words if sorted(list(i)) == sorted(list(word))]

print(filter_anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']))


# # TESTS - просто размести их под кодом
# assert filter_anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']) == ['aabb', 'bbaa']
# assert filter_anagrams('отсечка', ['сеточка', 'стоечка', 'тесачок', 'чесотка']) == ['сеточка', 'стоечка', 'тесачок', 'чесотка']
# assert filter_anagrams('tommarvoloriddle', ['iamlordvoldemort', 'iamdevolremort', 'mortmortmortmort', 'remortvolremort']) == ['iamlordvoldemort']
# assert filter_anagrams('стекло', []) == []
# assert filter_anagrams('крона', ['кротко', 'укроп', 'норка']) == ['норка']
# assert filter_anagrams('чулки', ['лучик', 'чутко', 'кочка']) == ['лучик']
# assert filter_anagrams('клоун', ['колдун', 'кулон', 'уклон', 'кол']) == ['кулон', 'уклон']
# assert filter_anagrams('abba', ['aaab', 'dbcd', 'bdaa', 'badb']) == []
# print('TESTS_OK')  # если распечатался TESTS_OK, значит все ОК )