import csv

with open('data_gen.csv', 'r', encoding='utf-8') as file:
    file_lines = (line for line in file)
    file_header = next(file_lines)
    file_values = (line.rstrip().split(',') for line in file_lines)
    result = 0
    for i in file_values:
        if i[2] == 'a':
            result += int(i[1])
    print(result)
