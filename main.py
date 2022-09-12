from converters import month_to_string, weekday_to_string
import datetime
# import os
from pygame.time import Clock
import ScheduleClass


def event_notification(schedule):
    events_time = {
        # Первая пара
        # 1/2
        '08:10:00': "Первая пара",
        # перерыв
        '08:55:00': "Перерыв",
        # 2/2
        '09:00:00': "Вторая часть первой пары",
        # конец
        '09:45:00': "Перемена",

        # Вторая пара
        # 1/2
        '09:55:00': "Вторая пара",
        # перерыв
        '10:40:00': "Перерыв",
        # 2/2
        '10:45:00': "Вторая часть второй пары",
        # конец
        '11:30:00': "Перемена",

        # Третья пара
        # 1/2
        '11:40:00': "Третья пара",
        # перерыв
        '12:25:00': "Перерыв",
        # 2/2
        '12:30:00': "Вторая часть третьей пары",
        # конец
        '13:15:00': "Перемена",

        # Четвертая пара
        # 1/2
        '13:35:00': "Четвёртая пара",
        # перерыв
        '14:20:00': "Перерыв",
        # 2/2
        '14:25:00': "Вторая часть четвёртой пары",
        # конец
        '15:10:00': "Перемена"
    }

    for key, value in events_time.items():
        hour, minute, second = map(int, key.split(":"))
        event_time = datetime.time(hour, minute, second)
        if schedule.time > event_time:
            time_to_event = schedule.div_time([hour, minute, second])
            break
    else:
        return "Пары кончились!"

    return f"{events_time[str(event_time)]} начнётся через: {str(time_to_event)}", str(event_time)


def console_output(schedule):
    def output_header():
        print(f"Сегодня {schedule.day} {month_to_string(schedule.month)} {schedule.time.replace(microsecond=0)}")

    def weekend_decoration():
        print("---Сегодня выходной!---")
        print(f"\n===Расписание на Понедельник===")

    def weekday_decoration():
        print(f"\n---Расписание на {weekday_to_string()['special'][current_weekday]}---")

    def classes_decoration():
        pass

    current_weekday = schedule.get_weekday()
    time_to_event, event_time = event_notification(schedule)
    output_header()
    print(time_to_event)
    if current_weekday in [6, 7]:
        weekend_decoration()
    else:
        weekday_decoration()


def main():
    schedule = ScheduleClass.SC()
    console_output(schedule)


if __name__ == '__main__':
    while True:
        print("\n"*30)
        main()
        # os.system('cls')
        Clock().tick(1)
