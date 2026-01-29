def get_min_max(data):
    if data == None:
        return None
    else:
        min_value = data.index(min(data))
        max_value = data.index(max(data))
        return (min_value, max_value)
    
data = [2, 3, 8, 1, 7]

print(get_min_max(data))    