class TextHandler:
    def __init__(self):
        self.words = []

    def add_words(self, text):
        self.words.append(text)
        return self.words

    def get_shortest_words(self):
        min_words = []
        res = min([len(w)for w in self.words])
        for w in self.words:
            if len(w) == res:
                min_words.append(w)
        return min_words

    def get_longest_words(self):
        res = max([len(w)for w in self.words])
        return list(w for w in self.words if len(w) == res)
    

texthandler = TextHandler()

texthandler.add_words('do not be sorry')
texthandler.add_words('be')
texthandler.add_words('better')

