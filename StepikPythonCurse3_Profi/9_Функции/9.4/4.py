def remove_marks(text, marks):
    remove_marks.__dict__.setdefault('count', 0)
    for i in marks:
        text = text.replace(i, '')
    remove_marks.count += 1
    return text
    

text = 'Hi! Will we go together?'

print(remove_marks(text, '!?'))
print(remove_marks.count)