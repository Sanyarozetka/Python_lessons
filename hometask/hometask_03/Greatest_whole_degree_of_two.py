"""
По данному натуральному числу N найдите наибольшую целую степень двойки, не превосходящую N. Выведите показатель степени
и саму степень. Операцией возведения в степень пользоваться нельзя!

50          5 32            2 ** 5 = 32
10          3 8             2 ** 3 = 8
8           3 8             2 ** 3 = 8
7           2 4             2 ** 2 = 4
1           0 1             2 ** 0 = 1
2           1 2             2 ** 1 = 2
3           1 2             2 ** 1 = 2
4           2 4             2 ** 2 = 4
5           2 4             2 ** 2 = 4
100         6 64            2 ** 6 = 64
1025        10 1024         2 ** 10 = 1024
15431543    23 8388608      2 ** 23 = 8388608
"""

n = int(input("Введите число: "))
print(n, end='   ')
k = 1
i = 2
d = 2
if n == 1:
    k = 0
    i = 1
else:
    while i * d <= n:
        i *= d
        k += 1

print(k, end=' ')
print(i, end='     ')
print(str(2) + ' ** ' + str(k) + ' = ' + str(i))