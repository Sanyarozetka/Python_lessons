"""
Дана строка. Замените в этой строке все появления буквы `h` на букву `H`, кроме первого и последнего вхождения.
Понадобятся: срезы и функция replace().
"""

string = input("Введите строку на английском: ")
s1 = string.replace("h", "H")
s2 = s1.replace("H", "h", 1)
s2_reverse = s2[::-1]
s3 = s2_reverse.replace("H", "h", 1)
s_finished = s3[::-1]
print(s_finished)
