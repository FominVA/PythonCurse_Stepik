
def hash_as_key(objects):
    dictinary = {}
    for object in objects:
        hash_object = hash(object)
        if hash_object not in dictinary:
            dictinary[hash_object] = object
        else:
            existing_value = dictinary[hash_object]
            if isinstance(existing_value, list):
                existing_value.append(object)
            else:
                dictinary[hash_object] = [existing_value, object]
    return dictinary

data = [1, 2, 3, 4, 5, 5]

print(hash_as_key(data))