def recursive_sum(nested_lists):
    if len(str(nested_lists)) == 0:
        return 0
    elif type(nested_lists) == int:
        return nested_lists
    else:
        if isinstance(nested_lists, list):
            total_sum = 0
            for element in nested_lists:
                total_sum += recursive_sum(element)
            return total_sum
        
my_list = [1, [4, 4], 2, [1, [2, 10]]]

print(recursive_sum(my_list))