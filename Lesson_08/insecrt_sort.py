from random import randint
from string import ascii_uppercase


def insert_sort(array1, array2):
    for i in range(len(array1)):
        tmp = array1[i]
        for j in range(i - 1, -1, -1):
            if tmp >= array1[j]:   # если >= то устойчивый, если без =, то не устойчивый
                break

            array1[j + 1], array1[j] = array1[j], array1[j + 1]
            array2[j + 1], array2[j] = array2[j], array2[j + 1]


# lst_1 = [randint(10, 99) for _ in range(25)]
lst_1 = [81, 13, 71, 62, 17, 12, 46, 10, 30, 22, 36, 64, 16, 71, 91, 56, 44, 27, 91, 94, 36, 26, 52, 58, 71]
lst_2 = list(ascii_uppercase[:25])


for n in range(len(lst_1)):
    print('{:4}'.format(lst_1[n]), end='')
print()

for k in range(len(lst_2)):
    print('{:>4}'.format(lst_2[k]), end='')
print()


insert_sort(lst_1, lst_2)

for n in range(len(lst_1)):
    print('{:4}'.format(lst_1[n]), end='')
print()

for k in range(len(lst_2)):
    print('{:>4}'.format(lst_2[k]), end='')
print()
