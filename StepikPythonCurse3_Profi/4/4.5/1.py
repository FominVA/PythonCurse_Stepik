from zipfile import ZipFile

with ZipFile('workbook.zip', mode='r') as zip_file:
    info = zip_file.infolist()
    
    count = 0
    for i in info:
        if i.is_dir()==False:
            count +=1
    print(count)