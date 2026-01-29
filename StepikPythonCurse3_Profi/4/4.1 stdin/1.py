import sys

for line in sys.stdin:
    sys.stdout.write('\n' + line.strip()[::-1])