from numerator_denominator import numerator, denominator
import datetime


class ScheduleClass:
    """
    Аттрибуты объекта:
        schedule = текущее расписание (Числитель / Знаменатель)
        current_date = текущая дата с точностью до миллисекунд
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
        return (self.start_date.weekday() + self.delta.days) % 7 + 1

    def is_numerator(self):
        # Возвращает True, если сегодня "числитель"
        return ((self.start_date.weekday() + self.delta.days) // 7) % 2 == 0


def console_decor(schedule):
    weekday_converter = {
        1: "Понедельник",
        2: "Вторник",
        3: "Среда",
        4: "Четверг",
        5: "Пятница",
        6: "Суббота",
        7: "Воскресенье"
    }

    if schedule.get_weekday() in [6, 7]:
        print(f"---Сегодня Выходной!---")
        print("Расписание на понедельник пока не реализовано :с")
        return
    else:
        current_weekday = schedule.get_weekday()
        print(f"---Сегодня {weekday_converter[current_weekday]}---")

    for time, couple in schedule.schedule[schedule.get_weekday()].items():
        print(time, *couple if couple is not None else 'ПАРЫ НЕТ!')


def main():
    schedule = ScheduleClass()
    if not schedule.is_numerator():
        schedule.schedule = denominator()

    console_decor(schedule)


if __name__ == '__main__':
    main()
