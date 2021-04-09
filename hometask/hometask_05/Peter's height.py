"""
Петя перешёл в другую школу. На уроке физкультуры ему понадобилось определить своё место в строю. Помогите ему это
сделать.

Программа получает на вход невозрастающую последовательность натуральных чисел, означающих рост каждого человека в
строю. После этого вводится число X – рост Пети. Все числа во входных данных натуральные и не превышают 200.
Выведите номер, под которым Петя должен встать в строй. Если в строю есть люди с одинаковым ростом, таким же, как у
Пети, то он должен встать после них.
Подсказки:

1. Здесь понадобится сортировка. Вот пример:
a = [5, 8, 2, 8, 4, 7, 0, 3, 1, 6, 9]
print(a)	# [5, 8, 2, 8, 4, 7, 0, 3, 1, 6, 9]
a.sort(reverse=True)
print(a)	# [9, 8, 8, 7, 6, 5, 4, 3, 2, 1, 0]
Параметр reverse=True отсортирует список в порядке убывания элементов.
2. Так же, понадобится list comprehension который позволит создать список случайных значений.
"""
import random


height_list = [round(random.randrange(150, 200)) for _ in range(30)]
height_list.sort(reverse=True)
print(height_list)
k = 1
height_of_student = (float(input("Введите рост Пети в см: ")))
if height_of_student <= 200:
    for i in range(len(height_list)):
        if height_of_student <= height_list[i]:
            k += 1
    print(k)
else:
    print("Введите число меньше чем 200")
