

tup = ()
print(tup, type(tup))
tup = tuple("Hello World!")
print(tup, type(tup))
lst = list(tup)
print(lst, type(lst))

tup = (1, 2, 3, 4, 4.6, 'test', False)
print(tup, type(tup))

t1 = (1, 2, 3)
t2 = (4, 5, 6)
t3 = t1 + t2
print(t3)
t4 = t3 * 4
print(t4)

t5 = 50, 68, 78
print(t5, type(t5))

a, b, c = t5
print(a, b, c)

a = t5[0]
b = t5[1]
c = t5[2]

print(a, b, c)
