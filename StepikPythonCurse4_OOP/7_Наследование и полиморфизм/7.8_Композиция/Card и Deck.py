from random import shuffle

class Card:
    suits = ['♣', '♢', '♡', '♠']
    ranks = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']

    def __init__(self, suit, rank):
            self.suit = suit
            self.rank = rank

    def __str__(self):
        return f'{self.suit}{self.rank}'

class Deck:
    def __init__(self):
        self.cards = [Card(suit, rank) for suit in Card.suits for rank in Card.ranks]

    def __str__(self):
        return f'Карт в колоде: {len(self.cards)}'

    def shuffle(self):
        if len(self.cards) != 52:
            raise ValueError('Перемешивать можно только полную колоду')
        shuffle(self.cards)

    def deal(self):
        if self.cards:
            return self.cards.pop(-1)
        else:
            raise ValueError("Все карты разыграны")
deck = Deck()

print(deck)
print(deck.deal())
print(deck.deal())
print(deck.deal())
print(type(deck.deal()))
print(deck)