import numpy as np

class Matrix:

    def __init__(self, rows: int, cols: int, value=0):
        self.rows = rows
        self.cols = cols
        self.data = [[value for _ in range(cols)] for _ in range(rows)]

    def get_value(self, row: int, col: int):
        return self.data[row][col]

    def set_value(self, row: int, col: int, value):
        self.data[row][col] = value

    def __str__(self):
        lines = []
        for row in self.data:
            lines.append(' '.join(map(str, row)))
        return '\n'.join(lines)

    def __repr__(self):
        return f'Matrix({self.rows}, {self.cols})'


    def __pos__(self):
        new_matrix = Matrix(self.rows, self.cols)
        new_matrix.data = [row[:] for row in self.data]
        return new_matrix

    def __neg__(self):
        new_matrix = Matrix(self.rows, self.cols)
        new_matrix.data = [[-item for item in row] for row in self.data]
        return new_matrix

    def __invert__(self):
        # Оператор ~ (транспонирование)
        # rows и cols меняются местами
        new_matrix = Matrix(self.cols, self.rows)
        # Используем zip для транспонирования данных
        new_matrix.data = [list(row) for row in zip(*self.data)]
        return new_matrix


    def __round__(self, n=None):
        # Функция round() для каждого элемента
        new_matrix = Matrix(self.rows, self.cols)
        new_matrix.data = [[round(item, n) for item in row] for row in self.data]
        return new_matrix

matrix = Matrix(2, 3, 1)

print(matrix)
print()
print(~matrix)