sum_numbers = 0
min_value = 0
max_value = 0
cnt = 0
odd = 0
even = 0

while True:
    num = int(input('Введите число: '))
    if num == 0:
        break

    cnt += 1
    sum_numbers += num
    if num % 2:
        even += 1
    else:
        odd += 1

    if cnt == 1:
        min_value = max_value = num

    if min_value > num:
        min_value = num

    if max_value < num:
        max_value = num

print('Сумма:', sum_numbers)
print('Кол-во:', cnt)
print('минимальное:', min_value)
print('Максимальное:', max_value)
print('Чётные:', odd)
print('Нечётные:', even)
print('Ср. арифм.:', round(sum_numbers/cnt, 2))
