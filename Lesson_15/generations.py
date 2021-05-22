
def gen_1(num):
    lst = []
    while num != 0:
        lst.append(num - 1)
        num -= 1
    return lst


# yield
def gen_2(num):
    while num != 0:
        yield num - 1
        num -= 1


print(gen_1(15))
print(gen_2(15))

for i in gen_2(15):
    print(i, end=' ')
print()

it = gen_2(5)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it, 999))
