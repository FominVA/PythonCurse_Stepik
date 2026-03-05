from datetime import date

class DateFormatter:

    def __init__(self, country_code):
        self.country_code = country_code

    def __call__(self, d):
        match self.country_code:
            case 'ru':
                return date.strftime(d, '%d.%m.%Y')
            case 'us':
                return date.strftime(d, '%m-%d-%Y')
            case 'ca':
                return date.strftime(d, '%Y-%m-%d')
            case 'br':
                return date.strftime(d, '%d/%m/%Y')
            case 'fr':
                return date.strftime(d, '%d.%m.%Y')
            case 'pt':
                return date.strftime(d, '%d-%m-%Y')
            
ru_format = DateFormatter('ru')

print(ru_format(date(2022, 11, 7)))