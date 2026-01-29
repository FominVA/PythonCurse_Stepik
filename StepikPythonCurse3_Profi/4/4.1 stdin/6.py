import sys

data = [word for word in sys.stdin.readlines() if not word.strip(' ').startswith('#')]

print(''.join(data))
        
