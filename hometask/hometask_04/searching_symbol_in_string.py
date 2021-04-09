"""
Пользователь вводит, отдельно, строку `s` и один символ `ch`.
Необходимо выполнить поиск в строке `s` всех символов `ch`.

Для решения НУЖНО использовать только функцию `find()`(rfind()), операторы `if` и `for`(while).

Старый, но рабочий код:

'for i in range(len(s)):
    b = s.find(ch, i)
    if b == i:
        print(b)
        i = b + 1
    else:
        continue'
"""

s = input("Введите строку: ")
ch = input("Введите искомый символ: ")
i = 0

while True:
    b = s.find(ch, i)
    if b == -1:
        break
    print(b)
    i = b + 1
