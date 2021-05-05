"""
    99, 31, 58, 65, 30, 46, 27, 41, 80
    27, 31, 58, 65, 30, 46, 99, 41, 80
    27, 30, 58, 65, 31, 46, 99, 41, 80
    27, 30, 31, 65, 58, 46, 99, 41, 80
    27, 30, 31, 41, 58, 46, 99, 65, 80
    27, 30, 31, 41, 46, 58, 99, 65, 80
    27, 30, 31, 41, 46, 58, 65, 99, 80
    27, 30, 31, 41, 46, 58, 65, 80, 99
"""
from random import randint

lst = [randint(10, 99) for _ in range(30)]
print(lst)


def select_sort(array):
    for i in range(len(array) - 1):
        m = i
        for j in range(i, len(array)):
            if array[j] > array[m]:
                m = j
        array[i], array[m] = array[m], array[i]


select_sort(lst)
print(lst)
