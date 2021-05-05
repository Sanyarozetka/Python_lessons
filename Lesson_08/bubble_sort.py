from random import randint

lst = [randint(10, 99) for _ in range(30)]

print(lst)


def bubble_sort(array):
    cnt = 0
    for i in range(len(array)-1):
        cnt += 1
        flag = True
        for j in range(len(array) - 1 - i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1],  array[j]
                flag = False
        if flag:
            break
    print("Кол-во проходов по списку: ", cnt)


bubble_sort(lst)
print(lst)
