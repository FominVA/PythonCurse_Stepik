import json
import sys

data = json.load(sys.stdin)
for key, value in data.items():
    if isinstance(value, list):
        print(key)
    else:
        print(key, value, sep=': ')