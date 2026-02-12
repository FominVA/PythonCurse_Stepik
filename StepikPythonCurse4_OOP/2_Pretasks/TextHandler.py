class TextHandler:
    def __init__(self):
        self.words = []

    def add_words(self, text):
        self.words.extend(text.split())
        
    def get_shortest_words(self):
        if not self.words:
            return []
        
        min_length = min(len(word) for word in self.words)
        return [word for word in self.words if len(word) == min_length]
    

    def get_longest_words(self):
        if not self.words:
            return []
        
        max_length = max(len(word) for word in self.words)
        return [word for word in self.words if len(word) == max_length]
    

texthandler = TextHandler()

texthandler.add_words('do not be sorry')
texthandler.add_words('be')
texthandler.add_words('better')

