class Wordplay:
    def __init__(self, words=[]):
        self.words = words.copy()

    def add_word(self, word):
        if word not in self.words:
            self.words.append(word)

    def words_with_length(self, n):
        return [word for word in self.words if len(word) == n]

    def only(self, *args):
        return [word for word in self.words if all(char in args for char in word)]
            
    def avoid(self, *args):
        return [word for word in self.words if all(char in args for char in word) == False]
