"""
Написать функцию is_year_leap, принимающую 1 аргумент — номер года, и возвращающую True, если год високосный,
и False иначе.
"""

year_in = int(input("Введите год: "))


def is_year_leap(year):
    if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
        return True
    else:
        return False


print(is_year_leap(year_in))
