import datetime


def event_notification(time):
    events_time = {
        # Первая пара
        # 1/2
        '08:10:00': "1/2 первой пары",
        # перерыв
        '08:55:00': None,
        # 2/2
        '09:00:00': None,
        # конец
        '09:45:00': None,

        # Вторая пара
        # 1/2
        '09:55:00': None,
        # перерыв
        '10:40:00': None,
        # 2/2
        '10:45:00': None,
        # конец
        '11:30:00': None,

        # Третья пара
        # 1/2
        '11:40:00': None,
        # перерыв
        '12:25:00': None,
        # 2/2
        '12:30:00': None,
        # конец
        '13:15:00': None,

        # Четвертая пара
        # 1/2
        '13:35:00': None,
        # перерыв
        '14:20:00': None,
        # 2/2
        '14:25:00': None,
        # конец
        '15:10:00': None
    }
    events = {}

    for key, value in events_time.items():
        h, m, s = map(int, key.split(":"))
        if time < datetime.time(h, m, s):
            time_to_event = datetime.datetime(h, m, s)
            break


def main():
    event_notification(datetime.datetime.now().time())


if __name__ == '__main__':
    main()
