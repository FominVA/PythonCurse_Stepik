def print_operation_table(operation, rows, cols):
    for n in range(1, rows+1):
        row_value = []
        for m in range(1, cols+1):
            matrix = operation(n, m)
            row_value.append(str(matrix))
        print(' '.join(row_value))
print_operation_table(lambda a, b: a * b, 5, 5)