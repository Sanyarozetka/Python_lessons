"""
Дан список чисел. Определите, сколько в нем встречается различных (уникальных) чисел.
  - Примечание. Эту задачу на Питоне можно решить в одну строчку.
(Задача решается с применением множеств)
"""

lst = [12, 45, 24, 33, 15, 45, 14, 38, 35, 37, 20, 48, 35, 25,
       26, 35, 43, 39, 29, 21, 29, 11, 14, 46, 29, 10, 11, 50, 37, 30]

print(len(set(lst)), set(lst))
