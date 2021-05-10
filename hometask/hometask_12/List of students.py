
"""
1. В текстовый файл (файл прилагается), построчно записаны имя и
фамилия учащихся класса и их оценки.
 Вывести на экран всех учащихся, чей средний балл меньше 5, также
посчитать и вывести средний балл по классу. Так же, записать в новый
файл всех учащихся в формате "Фамилия И.   Ср. балл":

 Говорухи А.        5.83
 Петров В.          4.92
 Варфаломеев Г.     5.92
 Тюльпанов И.       4.08
 Муромцев И.        5.42
 Бессмертный К.     5.5
 Мухин М.           6.92
 Мартынова М.       6.08
 Николаев П.        5.17
 Гусева Г.          5.83
 Тереньтьев С.      6.42
 Трердолобов С.     5.33

"""

file = open('src_14.txt', 'r', encoding='utf-8')
new_file = open('new_src_14.txt', 'w', encoding='utf-8')
lst_name = []
lst_marks = []
mid = 0
for line in file.readlines():
    name_surname = line[0:25:1]
    marks = line[25:66:1]
    lst_name.append(name_surname.split())
    lst_marks.append(marks.split())

for i in range(len(lst_name)):
    rating_lst = []
    s = lst_name[i][1] + ' ' + lst_name[i][0][0].upper() + '.'
    lst_marks[i] = [int(x) for x in lst_marks[i]]
    lst_marks.append(lst_marks[i])
    m = round(sum(lst_marks[i])/12, 2)
    tmp = '{:<20}{:<15}'.format(s, m)
    new_file.write(tmp + '\n')
    if m < 5:
        print(tmp)
    mid += m
print('Ср. балл по классу: - ' + str(round(mid / 12, 2)))
new_file.close()
file.close()
