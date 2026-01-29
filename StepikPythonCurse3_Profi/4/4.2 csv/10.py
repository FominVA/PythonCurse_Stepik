import csv

def condense_csv(filename, id_name):
    with open('data.csv', 'r', encoding='utf-8', newline='') as file1, open('condensed.csv', 'w', encoding='utf-8', newline='') as file2:
        reader = list(csv.reader(file1))
        d = {}
        for row in reader:
            d[row[0]] = d.setdefault(row[0], []) + row[1::]
        columns = [id_name]
        for value in d.values():
            for i in range(0, len(value), 2):
                if value[i] not in columns:
                    columns.append(value[i])
        writer = csv.writer(file2)
        writer.writerow(columns)
        for keys, values in d.items():
            line = [keys] + values[1::2]
            writer.writerow(line)


# TEST_2:
text = '''01,Artist,Otis Taylor
01,Title,Ran So Hard the Sun Went Down
01,Time,3:52
02,Artist,Waylon Jennings
02,Title,Honky Tonk Heroes (Like Me)
02,Time,3:29'''

with open('data.csv', 'w', encoding='utf-8') as file:
    file.write(text)

condense_csv('data.csv', id_name='ID')

with open('condensed.csv', encoding='utf-8') as file:
    print(file.read().strip())
