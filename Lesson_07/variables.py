y = 4


def summa(a, b):
    z = a + b + y
    return z


x = summa(3, 6)
print(x)


r = 50


def f():
    global r
    r = 30
    print(r)


print(r)
f()
print(r)
