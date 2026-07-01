class TicTacToe:
    def __init__(self):
        self.field = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        self._winner = None
        self.game_over = False
        self.current_player = 'X'

    def mark(self, x, y):
        if self.game_over:
            print('Игра окончена')
            return
        if not (1 <= x <= 3 and 1 <= y <= 3):
            print("Недоступная клетка")
            return
        row, col = x-1, y-1

        if self.field[row][col] != ' ':
            print("Недоступная клетка")
            return

        self.field[row][col] = self.current_player

        if self._check_winner():
            self.game_over = True
            self._winner = self.current_player
        else:
            if all(cell != ' ' for row in self.field for cell in row):
                self.game_over = True
                self._winner = 'Ничья'
            else:
                self.current_player = 'O' if self.current_player == 'X' else 'X'

    def show(self):
        result = []
        for i, row in enumerate(self.field):
            line = '|'.join(row)
            result.append(line)
            if i < 2:
                result.append('-'*5)
        print('\n'.join(result))

    def winner(self):
        return self._winner


    def _check_winner(self):
        for row in self.field:
            if row[0] == row[1] == row[2] and row[0] != ' ':
                return True

        for col in range(3):
            if self.field[0][col] == self.field[1][col] == self.field[2][col] and self.field[0][col] != ' ':
                return True

        if self.field[0][0] == self.field[1][1] == self.field[2][2] and self.field[0][0] != ' ':
            return True
        if self.field[0][2] == self.field[1][1] == self.field[2][0] and self.field[0][2] != ' ':
            return True
        return False

tictactoe = TicTacToe()

tictactoe.mark(1, 1)
tictactoe.mark(1, 3)
tictactoe.mark(3, 1)
tictactoe.mark(2, 1)

print(tictactoe.winner())

tictactoe.mark(3, 2)
tictactoe.mark(3, 3)
tictactoe.mark(1, 2)
tictactoe.mark(2, 2)
tictactoe.mark(2, 3)

print(tictactoe.winner())
tictactoe.show()
tictactoe.mark(2, 2)
print(tictactoe.winner())