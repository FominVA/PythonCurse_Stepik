from datetime import date, datetime

formats = {'ru': '%d.%m.%Y',
               'us': '%m-%d-%Y',
               'ca': '%Y-%m-%d',
               'br': '%d/%m/%Y',
               'fr': '%d.%m.%Y',
               'pt': '%d-%m-%Y'}

def date_formatter(country_code):
    def func(d):
        return datetime.strftime(d, formats[country_code])
    return func

date_ru = date_formatter('ru')
today = date(2022, 1, 25)
print(date_ru(today))