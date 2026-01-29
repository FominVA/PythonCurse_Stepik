from functools import lru_cache
import sys
lst = [s.strip() for s in sys.stdin]

@lru_cache(typed=True)
def sorted_word(word):
    return "".join(sorted(word))

for word in lst:
    print(sorted_word(word))
     
