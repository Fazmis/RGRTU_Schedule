from month_converter import month_converter
from datetime import datetime
import time
import ScheduleClass


def console_decor(schedule):
    weekday_converter = {
        "Именительный падеж": {
            1: "Понедельник",
            2: "Вторник",
            3: "Среда",
            4: "Четверг",
            5: "Пятница",
            6: "Суббота",
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

    print(f"Сегодня {weekday_converter['Именительный падеж'][current_weekday]}, "
          f"{schedule.day} {month_converter()[schedule.month]}\n")

    def weekend_corrector(day):
        if day in [6, 7]:
            print(f"---Сегодня Выходной!---")
            day = 1
            schedule.switch_numerator_denominator()
            print("Расписание на Понедельник!")
        else:
            print(f"\n---Расписание на {weekday_converter['Родительный падеж'][current_weekday]}---")
        return day

    time = schedule.current_date
    # Первая пара
    if time < datetime(schedule.year, schedule.month, schedule.day, 8, 10, 00):
        print(f"До начала первой пары: {datetime(schedule.year, schedule.month, schedule.day, 8, 10, 00) - time}")
    elif time < datetime(schedule.year, schedule.month, schedule.day, 8, 55, 00):
        print(f"Сейчас 1/2 первая пара, перерыв начнётся через: "
              f"{datetime(schedule.year, schedule.month, schedule.day, 8, 55, 00) - time}")
    elif time < datetime(schedule.year, schedule.month, schedule.day, 9, 40, 00):
        print(f"Сейчас 2/2 первая пара, перемена начнётся через: "
              f"{datetime(schedule.year, schedule.month, schedule.day, 9, 40, 00) - time}")
    # Вторая пара
    elif time < datetime(schedule.year, schedule.month, schedule.day, 9, 55, 00):
        print(f"Сейчас ПЕРЕМЕНА, вторая пара начнётся через: "
              f"{datetime(schedule.year, schedule.month, schedule.day, 9, 55, 00) - time}")
    elif time < datetime(schedule.year, schedule.month, schedule.day, 10, 40, 00):
        print(f"Сейчас 1/2 вторая пара, перерыв начнётся через: "
              f"{datetime(schedule.year, schedule.month, schedule.day, 10, 40, 00) - time}")
    elif time < datetime(schedule.year, schedule.month, schedule.day, 11, 30, 00):
        print(f"Сейчас 2/2 вторая пара, перемена начнётся через: "
              f"{datetime(schedule.year, schedule.month, schedule.day, 11, 30, 00) - time}")
    # третья пара
    elif time < datetime(schedule.year, schedule.month, schedule.day, 11, 40, 00):
        print(f"Сейчас ПЕРЕМЕНА, третья пара начнётся через: "
              f"{datetime(schedule.year, schedule.month, schedule.day, 11, 40, 00) - time}")
    elif time < datetime(schedule.year, schedule.month, schedule.day, 12, 25, 00):
        print(f"Сейчас 1/2 третья пара, перерыв начнётся через: "
              f"{datetime(schedule.year, schedule.month, schedule.day, 12, 25, 00) - time}")
    elif time < datetime(schedule.year, schedule.month, schedule.day, 13, 15, 00):
        print(f"Сейчас 2/2 третья пара, перемен начнётся через: "
              f"{datetime(schedule.year, schedule.month, schedule.day, 13, 15, 00) - time}")
    # Четвёртая пара
    elif time < datetime(schedule.year, schedule.month, schedule.day, 13, 35, 00):
        print(f"Сейчас ПЕРЕМЕНА, четвёртая пара начнётся через: "
              f"{datetime(schedule.year, schedule.month, schedule.day, 13, 35, 00) - time}")
    elif time < datetime(schedule.year, schedule.month, schedule.day, 14, 20, 00):
        print(f"Сейчас 1/2 четвёртая пара, перерыв начнётся через: "
              f"{datetime(schedule.year, schedule.month, schedule.day, 14, 20, 00) - time}")
    elif time < datetime(schedule.year, schedule.month, schedule.day, 15, 10, 00):
        print(f"Сейчас 2/2 четвёртая пара, КОНЕЦ пар через: "
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
    schedule = ScheduleClass.SC()
    console_decor(schedule)


if __name__ == '__main__':
    while True:
        main()
        time.sleep(1)
        print("\n"*120)
