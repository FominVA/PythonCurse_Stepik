
class CardDeck:
    def __init__(self):
        self.cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "валет", "дама", "король", "туз"]
        self.suits = ["пик", "треф", "бубен", "червей"]

        self.full_deck = []

        for suit in self.suits:
            for card in self.cards:
                self.full_deck.append(f'{card} {suit}')
        self.counter = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.counter < len(self.full_deck):
            result = self.full_deck[self.counter]
            self.counter += 1
        else:
            raise StopIteration
        return result 
        


cards = CardDeck()

print(next(cards))
print(next(cards))