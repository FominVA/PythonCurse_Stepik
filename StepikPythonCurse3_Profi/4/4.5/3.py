from zipfile import ZipFile

with ZipFile('workbook.zip') as zip_file:
    info = zip_file.infolist()
    l =[]
    for i in info:
        if i.is_dir()==False:
            before_comprassion = i.file_size
            after_compression = i.compress_size
            K = after_compression/before_comprassion
            l.append([i.filename, K])
    
    max_c = sorted(l, key= lambda x: x[1])
    print(max_c[0][0].split('/')[1])