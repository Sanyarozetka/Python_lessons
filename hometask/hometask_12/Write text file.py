"""
Создать текстовый файл, записать в него, построчно, данные которые вводит пользователь.
Окончанием ввода служит пустая строка.
Каждая введённая строка, в файле, должна начинаться с новой строки.
"""

file = open('new_file.txt', 'w', encoding='utf-8')
while True:
    line = input()
    if line == '':
        break
    file.write(line + '\n')
file.close()
