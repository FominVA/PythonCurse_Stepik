func = input()
a, b = map(int, input().split())
min_value = min([eval(func) for x in range(a, b + 1)])
max_value = max([eval(func) for x in range(a, b + 1)])
print(f'Минимальное значение функции {func} на отрезке [{a}; {b}] равно {min_value}')
print(f'Максимальное значение функции {func} на отрезке [{a}; {b}] равно {max_value}')

