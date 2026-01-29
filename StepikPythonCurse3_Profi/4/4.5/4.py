from zipfile import ZipFile

with ZipFile('workbook.zip') as zip_file:
    info = zip_file.infolist()
    l =[]
    my_datetime = (2021, 11, 30, 14, 22, 0)
    for i in info:
        if i.is_dir()==False and i.date_time > my_datetime:
            l.append(i.filename.split('/')[-1])
    
    print(*sorted(l), sep='\n')