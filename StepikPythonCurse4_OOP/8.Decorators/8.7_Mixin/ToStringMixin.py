class ToStringMixin:
    def __repr__(self):
        attrs = self.__dict__
        attr_count = len(attrs)
        if attr_count > 6:
            first_six = list(attrs.items())[:6]
            formated_six = ', '.join(f"{repr(k)}: {repr(v)}" for k, v in first_six)
            result = f'{formated_six}, ...'
        else:
            result = ', '.join(f"{repr(k)}: {repr(v)}" for k, v in attrs.items())
        return f'{self.__class__.__name__}({{{result}}})'

class Movie(ToStringMixin):
    def __init__(self, title, director, rating):
        self.title = title
        self._director = director
        self.__rating = rating

class Book(ToStringMixin):
    def __init__(self, title, author, publication_year, genre, pages, language, publisher):
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self.genre = genre
        self.pages = pages
        self.language = language
        self.publisher = publisher

book = Book('The Hobbit', 'J.R.R. Tolkien', 1937, 'Fantasy', 310, 'English', 'George Allen & Unwin')
print(book)