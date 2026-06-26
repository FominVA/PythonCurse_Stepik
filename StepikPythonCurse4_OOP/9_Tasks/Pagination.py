class Pagination:
    def __init__(self, iterable, pages):
        self.iterable = iterable
        self.pages = pages
        self.current_page = 1
        total_items = len(iterable)
        self.total_pages = (total_items + pages - 1) // pages if total_items > 0 else 1

    def _get_page_range(self, page_num):
        """Возвращает индексы [start, end) для заданной страницы (нумерация страниц с 1)."""
        start = (page_num - 1) * self.pages
        end = start + self.pages
        return start, end

    def get_visible_items(self):
        start, end = self._get_page_range(self.current_page)
        return self.iterable[start:end]

    def prev_page(self):
        if self.current_page > 1:
            self.current_page -= 1
        return self

    def next_page(self):
        if self.current_page < self.total_pages:
            self.current_page += 1
        return self

    def first_page(self):
        self.current_page = 1
        return self

    def last_page(self):
        self.current_page = self.total_pages
        return self

    def go_to_page(self, page):
        if page < 1:
            self.current_page = 1
        elif page > self.total_pages:
            self.current_page = self.total_pages
        else:
            self.current_page = page
        return self

text = '''У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кощей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.'''.splitlines()

pagination = Pagination(text, 5)
print(pagination.get_visible_items())