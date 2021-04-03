"""
Программа запрашивает ввод, с клавиатуры, целые числа, пока не будет введён 0. Как только будет введён 0 (ноль),
программа должна посчитать и вывести на экран:

- количество введённых чисел (завершающий 0 не считается)
- их сумму
- среднее арифметическое всех введённых чисел(не считая завершающего числа 0)
- определить максимальное и минимальное значение
- определить количество чётных и не чётных элементов в последовательности
"""

quantity = 0
amount = 0
# num_list = []
#
q_even = 0
q_uneven = 0
num_min = 0
num_max = 0
while True:
    num = int(input("Введите число: "))
    if num == 0:
        break
    quantity += num
    amount += 1
    # num_list += [num]
    #
    if num_max == 0:
        num_max = num
        num_min = num
    if num > num_max:
        num_max = num
    elif num < num_min:
        num_min = num
    if num % 2 == 0:
        q_even += 1
    else:
        q_uneven += 1

print("Количество введённых чисел " + str(amount))
print("Сумма введённых чисел " + str(quantity))
print("Cреднее арифметическое всех введённых чисел " + str(quantity / amount))
# print("Максимальное значение " + str(max(num_list)))
# print("Минимальное значение " + str(min(num_list)))
print("Максимальное значение " + str(num_max))
print("Минимальное значение " + str(num_min))
print("Количество чётных элементов " + str(q_even))
print("количество не чётных элементов " + str(q_uneven))
