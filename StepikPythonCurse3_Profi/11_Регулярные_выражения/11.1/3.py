from re import search, MULTILINE
from sys import stdin

data = [line.strip() for line in stdin]

pattern_URL = r'<p><a href="(\w+://\w+.\w+)">(<b>\w+</b>)</a></p>|<p><a href="(\w+://\w+.\w+)">(\w+)</a></p>'

for word in data:
    match =  search(pattern_URL, word)
    print(match.groups())
