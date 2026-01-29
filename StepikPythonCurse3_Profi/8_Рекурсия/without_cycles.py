def without_cycles(n):
    if n > 0:
        print(n)
        without_cycles(n-5)
    print(n)

without_cycles(int(input()))