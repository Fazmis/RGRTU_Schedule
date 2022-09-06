from numerator_denominator import numerator, denominator
from datetime import datetime


class ScheduleClass:
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


def console_decor(schedule):
    weekday_converter = {
        "Именительный падеж": {
            1: "Понедельник",
            2: "Вторник",
            3: "Среду",
            4: "Четверг",
            5: "Пятницу",
            6: "Субботу",
            7: "Воскресенье"
        },
        "Родительный падеж": {
            1: "Понедельник",
            2: "Вторник",
            3: "Среду",
            4: "Четверг",
            5: "Пятницу",
            6: "Субботу",
            7: "Воскресенье"
        }
    }

    current_weekday = schedule.get_weekday()

    print(f"Сегодня {weekday_converter['Родительный падеж'][current_weekday]}")

    def weekend_corrector(day):
        if day in [6, 7]:
            print(f"---Сегодня Выходной!---")
            day = 1
            schedule.switch_numerator_denominator()
            print("Расписание на Понедельник!")
        else:
            print(f"---Расписание на {weekday_converter['Именительный падеж'][current_weekday]}---")
        return day

    time = schedule.current_date
    # Первая пара
    if time < datetime(schedule.year, schedule.month, schedule.day, 8, 10, 00):
        print(f"До начала первой пары: {datetime(schedule.year, schedule.month, schedule.day, 8, 10, 00) - time}")
    elif time < datetime(schedule.year, schedule.month, schedule.day, 9, 40, 00):
        print(f"Сейчас первая пара, вторая начнётся через: "
              f"{datetime(schedule.year, schedule.month, schedule.day, 9, 55, 00) - time}")
    # Вторая пара
    elif time < datetime(schedule.year, schedule.month, schedule.day, 9, 55, 00):
        print(f"Сейчас ПЕРЕМЕНА, вторая пара начнётся через: "
              f"{datetime(schedule.year, schedule.month, schedule.day, 9, 55, 00) - time}")
    elif time < datetime(schedule.year, schedule.month, schedule.day, 11, 30, 00):
        print(f"Сейчас вторая пара, третья пара начнётся через: "
              f"{datetime(schedule.year, schedule.month, schedule.day, 11, 40, 00) - time}")
    # третья пара
    elif time < datetime(schedule.year, schedule.month, schedule.day, 11, 40, 00):
        print(f"Сейчас ПЕРЕМЕНА, третья пара начнётся через: "
              f"{datetime(schedule.year, schedule.month, schedule.day, 11, 40, 00) - time}")
    elif time < datetime(schedule.year, schedule.month, schedule.day, 13, 15, 00):
        print(f"Сейчас третья пара, четвёртая пара начнётся через: "
              f"{datetime(schedule.year, schedule.month, schedule.day, 13, 35, 00) - time}")
    # Четвёртая пара
    elif time < datetime(schedule.year, schedule.month, schedule.day, 13, 35, 00):
        print(f"Сейчас ПЕРЕМЕНА, четвёртая пара начнётся через: "
              f"{datetime(schedule.year, schedule.month, schedule.day, 13, 35, 00) - time}")
    elif time < datetime(schedule.year, schedule.month, schedule.day, 15, 10, 00):
        print(f"Сейчас четвёртая пара, КОНЕЦ пар через: "
              f"{datetime(schedule.year, schedule.month, schedule.day, 15, 10, 00) - time}")
    # После пар
    elif time > datetime(schedule.year, schedule.month, schedule.day, 15, 10, 00):
        print(f"Пары кончились :3")
        current_weekday += 1
    else:
        print("Error")

    current_weekday = weekend_corrector(current_weekday)

    for couple_start_time, couple in schedule.schedule[current_weekday].items():
        print(couple_start_time, *couple if couple is not None else 'ПАРЫ НЕТ!')


def main():
    schedule = ScheduleClass()
    console_decor(schedule)


if __name__ == '__main__':
    main()
