import datetime

class WeatherWarning:
    def rain(self):
        print('Ожидаются сильные дожди и ливни с грозой')

    def snow(self):
        print('Ожидается снег и усиление ветра')

    def low_temperature(self):
        print('Ожидается сильное понижение температуры')

class WeatherWarningWithDate(WeatherWarning):
    def rain(self, time):
        print(datetime.date.strftime(time, '%d.%m.%Y'))
        print('Ожидаются сильные дожди и ливни с грозой')

    def snow(self, time):
        print(datetime.date.strftime(time, '%d.%m.%Y'))
        print('Ожидается снег и усиление ветра')

    def low_temperature(self, time):
        print(datetime.date.strftime(time, '%d.%m.%Y'))
        print('Ожидается сильное понижение температуры')