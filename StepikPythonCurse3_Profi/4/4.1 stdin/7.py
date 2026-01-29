import sys
text=[line.strip().split('/') for line in sys.stdin]
tema=text[-1][0].strip()
text.pop(-1)
new_text = sorted(text, key=lambda x:(x[2], x[0]))

for i in new_text:
    if tema in i[1]:
        print(i[0].strip(), sep='\n')