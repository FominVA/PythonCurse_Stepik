class FieldTracker:
    def __init__(self):
        # Исходные значения атрибутов
        self._original_values = {
            field: getattr(self, field) for field in self.fields
        }
        # Список изменённых полей в порядке их первого изменения
        self._changed_order = []
        # Множество для быстрой проверки, было ли поле уже отмечено как изменённое
        self._changed_set = set()

    def base(self, atr):
        if atr in self._changed_set:
            return self._original_values[atr]
        else:
            return getattr(self, atr)

    def has_changed(self, atr):
        return atr in self._changed_set

    def changed(self):
        # Формируем словарь в порядке первого изменения полей
        result = {}
        for field in self._changed_order:
            if field not in result:
                result[field] = self._original_values[field]
        return result

    def save(self):
        # Обновляем исходные значения до текущих
        for field in self.fields:
            self._original_values[field] = getattr(self, field)
        # Сбрасываем отслеживание изменений
        self._changed_order.clear()
        self._changed_set.clear()

    def __setattr__(self, name, value):
        # Проверяем, инициализирован ли трекер и отслеживается ли поле
        if hasattr(self, '_original_values') and name in self.fields:
            current_value = getattr(self, name, None)
            # Если значение изменилось
            if current_value != value:
                # Если поле ещё не отмечено как изменённое, добавляем в порядок и множество
                if name not in self._changed_set:
                    self._changed_order.append(name)
                    self._changed_set.add(name)
        # Устанавливаем атрибут
        super().__setattr__(name, value)

class Point(FieldTracker):
    fields = ('x', 'y', 'z')

    def __init__(self, x, y, z):
        self.x, self.y, self.z = x, y, z
        super().__init__()

point = Point(1, 2, 3)
point.x = 0
point.z = 4
point.z = 5

print(point.base('x'))
print(point.base('z'))
print(point.has_changed('x'))
print(point.has_changed('z'))
print(point.changed())






