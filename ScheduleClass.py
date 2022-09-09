from numerator_denominator import numerator, denominator
from datetime import datetime


class SC:
    """
    Аттрибуты объекта:
        schedule = текущее расписание (Числитель / Знаменатель)
        current_date = текущая дата с точностью до миллисекунд
        year = текущий год
        start_date = начало учебного года
        delta = количество месяцев, дней прошедших с начала учебного года до текущего момента
    """
    def __init__(self):
        def numerator_denominator_init():
            if ((self.start_date.weekday() + self.delta.days) // 7) % 2 == 0:  # Возвращает True, если сегодня числитель
                return numerator()
            else:
                return denominator()

        self.current_date = datetime.now()
        self.year = self.current_date.year
        self.month = self.current_date.month
        self.day = self.current_date.day
        if self.current_date >= datetime(self.year, 8, 31):
            self.start_date = datetime(self.year, 9, 1)
        else:
            self.start_date = datetime(self.year - 1, 9, 1)
        self.delta = self.current_date - self.start_date
        self.schedule = numerator_denominator_init()

    def get_daytime(self):
        # Возвращает текущее дневное время
        return self.current_date.time()

    def get_weekday(self):
        # Возвращает текущий день недели (1-7)
        return (self.start_date.weekday() + self.delta.days) % 7 + 1

    def switch_numerator_denominator(self):
        if self.schedule is numerator():
            self.schedule = denominator()
        else:
            self.schedule = numerator()
