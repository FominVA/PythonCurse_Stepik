from datetime import datetime
class LoggerMixin:
    def log(self, lvl, text):
        now = datetime.now().strftime("%d.%m.%Y %H:%M:%S")
        print(f"[{now}] - {lvl} - {self.__class__.__name__}: {text}")

class Database(LoggerMixin):
    def connect(self):
        self.log('INFO', 'Выполнено подключение к базе данных.')

    def disconnect(self):
        self.log('INFO', 'Подключение к базе данных закрыто.')

db = Database()
db.connect()
db.disconnect()