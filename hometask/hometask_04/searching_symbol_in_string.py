"""
Пользователь вводит, отдельно, строку `s` и один символ `ch`.
Необходимо выполнить поиск в строке `s` всех символов `ch`.

She couldn't lift a heavy box with her hamster

Для решения НУЖНО использовать только функцию `find()`(rfind()), операторы `if` и `for`(while).
"""
s = input("Введите строку: ")
ch = input("Введите искомый символ: ")

for i in range(len(s)):
    if s[i] == ch:
        print(s.find(ch, i))
        i += 1
    else:
        i += 1
