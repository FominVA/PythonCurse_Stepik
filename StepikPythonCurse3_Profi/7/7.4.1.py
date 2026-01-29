week = { 1: "Понедельник", 2: "Вторник", 3: "Среда", 4: "Четверг", 5: "Пятница", 6: "Суббота", 7: "Воскресенье"}
def get_weekday(numbers):
    if isinstance(numbers, int) == False:
        raise TypeError('Аргумент не является целым числом')
    if not (1<=numbers<=7):
        raise ValueError('Аргумент не принадлежит требуемому диапазону')
    return week[numbers]
    
      