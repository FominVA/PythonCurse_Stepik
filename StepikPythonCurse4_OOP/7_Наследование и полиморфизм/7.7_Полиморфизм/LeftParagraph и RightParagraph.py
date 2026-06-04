from abc import ABC, abstractmethod


class Paragraph(ABC):
    def __init__(self, length):
        self._size = length
        self._paragraph = ['']

    def add(self, words):
        words = words.split()
        for word in words:
            if len(self._paragraph[-1] + f' {word}') > self._size:
                self._paragraph.append('')
            self._paragraph[-1] = (self._paragraph[-1] + f' {word}').lstrip()

    @abstractmethod
    def end(self):
        pass


class LeftParagraph(Paragraph):
    def end(self):
        for line in self._paragraph:
            print(line)
        self._paragraph = ['']


class RightParagraph(Paragraph):
    def end(self):
        for line in self._paragraph:
            print(line.rjust(self._size))
        self._paragraph = ['']


rightparagraph = RightParagraph(10)

rightparagraph.add('death')
rightparagraph.add('can have me')
rightparagraph.add('when it earns me')
rightparagraph.end()