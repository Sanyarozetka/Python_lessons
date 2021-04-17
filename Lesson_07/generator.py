

def gen1(num):
    lst = []
    while num != 0:
        lst. append(num - 1)
        num -= 1

    return lst


print(gen1(10))

def gen2(num):
    while num != 0:
        yield num - 1
        num -= 1


for i in gen2(10):
    print(i, end=' ')
