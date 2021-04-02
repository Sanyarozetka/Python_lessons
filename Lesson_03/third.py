"""
if <condition>:
    operator 1
    operator 2
else:
    operator 3
    operator 4

if <condition>:
    operator 1
    operator 2
elif <condition>:
    operator 3
    operator 4
elif <condition>:
    operator 5
    operator 6
else:
    operator 7
"""

a = int(input("Введите число: "))
"""if 10 <= a <= 20:
    print('Number in range from 10 till 20')
else:
    print('Number out range from 10 till 20')

print('End program')
"""   # Задача 1


if a > 0:
    print('positive')
elif a < 0:
    print('negative')
else:
    print('zero')

print('End program')

res = 'Our number if range 10 to 20' if 10 <= a <= 20 else 'number is incorrect'
print(res)
