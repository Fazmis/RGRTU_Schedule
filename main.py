from numerator_denominator import numerator, denominator
import datetime


class ScheduleClass:
    """
    Свойства объекта:
        schedule = текущее расписание (Числитель / Знаменатель)
        current_date = текущая дата с максимальной точностью
        current_year = текущий год
        start_date = начало учебного года
        delta = количество месяцев, дней прошедших с начала учебного года до текущего момента
    """

    def __init__(self):
        self.schedule = numerator()
        self.current_date = datetime.datetime.now()
        self.current_year = self.current_date.year
        if self.current_date >= datetime.datetime(self.current_year, 8, 31):
            self.start_date = datetime.datetime(self.current_year, 9, 1)
        else:
            self.start_date = datetime.datetime(self.current_year - 1, 9, 1)
        self.delta = self.current_date - self.start_date

    def get_daytime(self):
        # Возвращает текущее дневное время
        return self.current_date.time()

    def get_weekday(self):
        # Возвращает текущий день недели (1-7)
        return (self.start_date.weekday() + 1 + self.delta.days) % 7

    def is_numerator(self):
        # Возвращает True, если сегодня "числитель"
        return ((self.start_date.weekday() + 1 + self.delta.days) // 7) % 2 == 0


def main():
    schedule = ScheduleClass()
    if not schedule.is_numerator():
        schedule.schedule = denominator()
    print(schedule.get_weekday())
    print(schedule.schedule[5])


if __name__ == '__main__':
    main()
