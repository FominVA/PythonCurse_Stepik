from sys import stdin
from collections import Counter

grades = Counter()

for line in stdin:
    name, grade = line.split(' ')
    grades[name] = int(grade)
print(grades.most_common()[-2][0])
