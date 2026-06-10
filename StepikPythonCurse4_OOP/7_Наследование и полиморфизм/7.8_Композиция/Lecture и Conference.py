import datetime

class Lecture:
    def __init__(self, topic, start_time, duration):
        self.topic = topic
        # Переводим строки в объекты time и timedelta
        self.start_time = datetime.datetime.strptime(start_time, '%H:%M').time()
        # Длительность в минутах (удобнее хранить как timedelta)
        hours, minutes = map(int, duration.split(':'))
        self.duration = datetime.timedelta(hours=hours, minutes=minutes)

    @property
    def end(self):
        # Вычисляем время окончания как datetime, но потом получаем time
        start_dt = datetime.datetime.combine(datetime.date.today(), self.start_time)
        end_dt = start_dt + self.duration
        return end_dt.time()

class Conference:
    def __init__(self):
        self.conf = []

    def add(self, lecture: Lecture):
        new_start = lecture.start_time
        new_end = lecture.start_time + lecture.duration
        for existing in self.conf:
            exist_start = existing.start_time
            exist_end = existing.start_time + existing.duration
            if new_start < exist_end and exist_start < new_end:
                raise ValueError("Провести выступление в это время невозможно")
        self.conf.append(lecture)

conference = Conference()
conference.add(Lecture('Простые числа', '08:00', '01:30'))

try:
    conference.add(Lecture('Жизнь после ChatGPT', '09:00', '02:00'))
except ValueError as error:
    print(error)
