"""
По данному целому числу N распечатайте все квадраты натуральных чисел, не превосходящие N, в порядке возрастания.

50      1 4 9 16 25 36 49
10      1 4 9
9       1 4 9
4       1 4
1       1
100     1 4 9 16 25 36 49 64 81 100
99      1 4 9 16 25 36 49 64 81
"""


n = int(input("Введите число: "))
print(n, end='     ')
i = 1
while i**2 <= n:
    print(i**2, end=' ')
    i += 1

print()
