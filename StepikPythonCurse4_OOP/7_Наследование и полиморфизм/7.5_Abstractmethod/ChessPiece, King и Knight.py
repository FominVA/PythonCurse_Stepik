from abc import abstractmethod, ABC

class ChessPiece(ABC):
    def __init__(self, horizontal: str, vertical: int):
        if isinstance(horizontal, str) and 97 <= ord(horizontal) <= 104:
            self.horizontal = horizontal
        if isinstance(vertical, int) and 0 < vertical < 9:
            self.vertical = vertical

    @abstractmethod
    def can_move(self, new_horizontal, new_vertical):
        cur_x = ord(self.horizontal) - ord('a') + 1
        cur_y = self.vertical
        new_x = ord(new_horizontal) - ord('a') + 1
        new_y = new_vertical
        dx = abs(cur_x-new_x)
        dy = abs(cur_y-new_y)
        return [dx, dy]

class King(ChessPiece):
    def can_move(self, new_horizontal, new_vertical):
        dx = super().can_move(new_horizontal, new_vertical)[0]
        dy = super().can_move(new_horizontal, new_vertical)[1]
        return (dx <= 1 and dy <= 1) and not (dx == 0 and dy == 0)

class Knight(ChessPiece):
    def can_move(self, new_horizontal, new_vertical):
        dx = super().can_move(new_horizontal, new_vertical)[0]
        dy = super().can_move(new_horizontal, new_vertical)[1]
        return (dx == 2 and dy == 1) or (dx == 1 and dy == 2)


king = King('b', 2)

print(king.can_move('c', 3))
print(king.can_move('a', 1))
print(king.can_move('f', 7))