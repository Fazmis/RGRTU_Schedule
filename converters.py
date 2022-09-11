def month_to_string(month=1):
	months = {
		1: "января",
		2: "февраля",
		3: "марта",
		4: "апреля",
		5: "мая",
		6: "июня",
		7: "июля",
		8: "августа",
		9: "сентября",
		10: "октября",
		11: "ноября",
		12: "декабря"
	}
	return months[month]


def weekday_to_string():
	weekdays = {
		"base": {
			1: "Понедельник",
			2: "Вторник",
			3: "Среда",
			4: "Четверг",
			5: "Пятница",
			6: "Суббота",
			7: "Воскресенье"
		},
		"special": {
			1: "Понедельник",
			2: "Вторник",
			3: "Среду",
			4: "Четверг",
			5: "Пятницу",
			6: "Субботу",
			7: "Воскресенье"
		}
	}
	return weekdays


def main():
	for data in [month_to_string(), weekday_to_string()]:
		print(data)


if __name__ == '__main__':
	main()
