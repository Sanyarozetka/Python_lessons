from random import random


def print_func(array):
    for i in range(len(array)):
        print(' ' + '  '.join("{:^3}".format(i) for i in array[i]))


m = int(input("Введите количество M элементов двухмерного списка MxN: "))
n = int(input("Введите количество N элементов двухмерного списка MxN: "))
a = []
for i in range(n):
    b = []
    c = 0
    for j in range(m):
        b.append(int(random() * 50))
        print("%4d" % b[j], end='')
        c += b[j]
    a.append(b)
    print('    ', c)

for i in range(m):
    print("    ", end='')
print()

for i in range(m):
    s = 0
    for j in range(n):
        s += a[j][i]
    print("%4d" % s, end='')
print()