def reverse_print():
    n = int(input())
    if n != 0:
        reverse_print()
    print(n)

reverse_print()