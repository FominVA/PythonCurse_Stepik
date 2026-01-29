def linear(nested_lists):
    lean_list = []
    if isinstance(nested_lists, int):
        return [nested_lists]
    else:
        if isinstance(nested_lists, list):
            for i in nested_lists:
                lean_list.extend(linear(i))
    return lean_list
    
my_list = [3, [4], [5, [6, [7, 8]]]]

print(linear(my_list))