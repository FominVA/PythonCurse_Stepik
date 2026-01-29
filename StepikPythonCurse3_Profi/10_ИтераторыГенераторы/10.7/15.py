def around(iterable):
    if type(data) != list:
        data = [i for i in data]
    for i in range(len(data)):
        try:
            yield (data[i],data[i+1])
        except:
            yield (data[i],None)    