from sys import stdin
from re import match, search
pattern1 = r'\d{[1-3]}'
pattern2 = r'( -)?\d|\d{2}|\d{3}( -)?'
pattern3 = r''

num = [i for i in stdin]

print(f'Код страны: {num}, Код города: 877, Номер: 2638277')
