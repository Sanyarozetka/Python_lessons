import random


PI = 3.14


def binary_search(array, key, left=0, right=None):
    if left < 0:
        raise ValueError('Левый индекс не может быть меньше 0')

    if right is None:
        right = len(array)

    middle = (left + right) // 2
    while array[middle] != key and left <= right:
        if array[middle] < key:
            left = middle + 1
        else:
            right = middle - 1

        middle = (left + right) // 2

    return (True, middle) if not (left > right) else (False, middle+1)


def func1():
    pass


def func2():
    pass


if __name__ == '__main__':
    lst = [random.randint(10, 99) for _ in range(25)]
    print(lst)
    lst.sort()
    print(lst)
    # print(__name__)
    value = int(input('Введите ключ: '))
    result = binary_search(lst, value)
    if result[0]:
        print(value, 'находится по индексу:', result[1])
    else:
        lst.insert(result[1], value)
        print(lst)
