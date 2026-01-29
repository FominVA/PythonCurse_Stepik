from zipfile import ZipFile

def extract_this(zip_name, *args):
    with ZipFile(zip_name) as zip_file:
        if not args:
            zip_file.extractall()
        else:
            for file_to_extract in args:
                zip_file.extract(file_to_extract)

