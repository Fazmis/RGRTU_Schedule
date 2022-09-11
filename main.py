from converters import month_to_string, weekday_to_string
from datetime import datetime
import os
import pygame
import time
import ScheduleClass


def console_output(schedule):
    def output_header():
        print(f"Сегодня {current_weekday} {month_to_string(schedule.month)} {schedule.time.replace(microsecond=0)}")

    def weekend_handler():
        print("---Сегодня выходной!---")
        print(f"\n===Расписание на Понедельник===")

    def weekday_handler():
        print(f"\n---Расписание на {weekday_to_string()['special'][current_weekday]}---")

    current_weekday = schedule.get_weekday()
    output_header()
    if current_weekday in [6, 7]:
        weekend_handler()
    else:
        weekday_handler()



def main():
    schedule = ScheduleClass.SC()
    console_output(schedule)


if __name__ == '__main__':
    while True:
        main()
        os.system('cls')
        pygame.time.Clock().tick(1)
