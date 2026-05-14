class TitledText(str):

    def __new__(cls, content, text_title):
        instance = super().__new__(cls, content)
        instance.text_title = text_title
        return instance


    def title(self):
        return self.text_title




titled = TitledText('Create a class Soda', 'Homework')

print(titled)
print(titled.title())
print(issubclass(TitledText, str))