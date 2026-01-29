from zipfile import ZipFile

with ZipFile('workbook.zip', mode='r') as zip_file:
    info = zip_file.infolist()
    before_comprassion = 0
    for i in range(len(info)):
        before_comprassion += info[i].file_size

    after_compression = 0
    for i in range(len(info)):
        after_compression += info[i].compress_size

    print(f'Объем исходных файлов: {before_comprassion} байт(а)')
    print(f'Объем сжатых файлов: {after_compression} байт(а)')

        