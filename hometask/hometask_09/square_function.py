"""
Написать функцию square, принимающую 1 аргумент — сторону квадрата, и возвращающую 3 значения (с помощью кортежа):
периметр квадрата, площадь квадрата и диагональ квадрата.
"""
side = float(input('Введите сторону квадрата: '))


def square(square_side):
    perimeter = round(square_side * 4, 2)
    area = round(square_side ** 2, 2)
    diagonal = round(square_side * (2 ** 0.5), 2)
    result = (perimeter, area, diagonal)
    return result


print(square(side))
