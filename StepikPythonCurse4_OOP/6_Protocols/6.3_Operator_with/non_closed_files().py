def non_closed_files(files):
    l = []
    for file in files:
        if not file.closed:
            l.append(file)
            return l