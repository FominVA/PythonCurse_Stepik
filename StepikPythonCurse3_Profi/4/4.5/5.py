from zipfile import ZipFile
from datetime import datetime
with ZipFile('workbook.zip') as zip_file:
    info = zip_file.infolist()
    names = []
    for i in info:
        if i.is_dir()==False:
            names.append([i.filename.split('/')[-1], i.date_time, i.file_size, i.compress_size])

    names = sorted(names, key= lambda x: x[0])
    c = 0
    for i in names:
        print(i[0])
        print(f'  Дата модификации файла: {datetime(*i[1])}')
        print(f'  Объем исходного файла: {i[2]} байт(а)')
        print(f'  Объем сжатого файла: {i[3]} байт(а)', sep='\n')
        c += 1
        if c < len(names):
            print()
# Alexandra Savior – Crying All the Time.mp3
#   Дата модификации файла: 2021-11-30 13:27:02
#   Объем исходного файла: 5057559 байт(а)
#   Объем сжатого файла: 5051745 байт(а)