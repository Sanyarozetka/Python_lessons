from random import randint


lst = [randint(10, 99) for _ in range(25)]

print(lst)
key = int(input("Что ищем: "))

for idx in range(len(lst)):
    if lst[idx] == key:
        print('Найден индекс:', idx)
        break
else:
    print('Элемент не найден')
