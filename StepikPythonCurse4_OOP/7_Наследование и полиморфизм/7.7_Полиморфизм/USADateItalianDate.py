from datetime import date

class USADate:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day
        self.data = date(self.year, self.month, self.day)

    def format(self):
        return self.data.strftime('%m-%d-%Y')


    def iso_format(self):
        return self.data

class ItalianDate(USADate):

    def format(self):
        return self.data.strftime('%d/%m/%Y')


usadate = USADate(2023, 4, 6)

print(usadate.format())
print(usadate.iso_format())