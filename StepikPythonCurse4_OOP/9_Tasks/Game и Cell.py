
class Cell:
    def __init__(self, row, col, mine=False):
        self.row = row
        self.col = col
        self.mine = mine
        self.neighbours = 0
        self.opened = False

class Game:
    def __init__(self, rows, cols, mines):
        self.rows = rows
        self.cols = cols
        self.mines = mines
        self.board = []
        for r in range(rows):
            row_cell = []
            for c in range(cols):
                cell = Cell(r, c)
                row_cell.append(cell)
            self.board.append(row_cell)

game = Game(2, 3, 4)
print(game.board)