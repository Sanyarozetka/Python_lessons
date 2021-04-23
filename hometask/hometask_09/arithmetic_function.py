"""
Написать функцию arithmetic, принимающую 3 аргумента: первые 2 - числа, третий - операция, которая должна быть
произведена над ними. Функция должна вернуть результат вычислений зависящий от третьего аргумент: +, сложить их; если -,
то вычесть; * — умножить; / — разделить (первое на второе). В остальных случаях вернуть строку "Неизвестная операция".
"""

numb_1 = float(input("Введите первое число: "))
numb_2 = float(input("Введите второе число: "))
operation = input("Введите операцию (+, -, *, /): ")


def arithmetic(num_1, num_2, operator):
    if operator == '+':
        return num_1 + num_2
    elif operator == '-':
        return num_1 - num_2
    elif operator == '*':
        return num_1 * num_2
    elif operator == '/':
        return num_1 / num_2
    else:
        return "Неизвестная операция"


print(arithmetic(numb_1, numb_2, operation))
