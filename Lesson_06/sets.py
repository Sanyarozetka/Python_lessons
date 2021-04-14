import random

s = set('Hello World!')
print(s, type(s))
s = set([1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5])
print(s, type(s))
# lst = []
d = {}
print(d, type(d))
s = {1, 2, 56, 7, 8}
print(s, type(s))

for elem in s:
    print(elem, end=' ')
print()

s.add(45)
print(s)

# len(set)
print(len(s))

# add(value)
s.add(8)
print(s)

# pop()
x = s.pop()
print(x, s)


a = {10, 12, 13, 15, 18, 19, 21, 22, 23, 25, 26, 28, 29, 32, 33, 34, 40, 42, 44, 46, 48, 50}
b = {34, 35, 37, 38, 40, 41, 10, 42, 11, 13, 14, 15, 47, 50, 20, 22, 27, 31}
# a = {random.randint(10, 50) for _ in range(30)}
# print(a)
print('len A:', len(a))
print('len B:', len(b))
# A | B      A.union(B)
# A |= B     A.update(B)

c = a | b
print(len(c), c)

# A & B    A.intersection(B)
# A &= B   A.intersection_update(B)
c = a & b
print(len(c), c)

# A - B      A.difference(B)
# A -= B     A.difference_update(B)
c = a - b
print(len(c), c)

# A ^ B     A.symmetric_difference(B)
# A ^= B     A.symmetric_difference_update(B)
c = a ^ b
print(len(c), c)
c1 = a - b
c2 = b - a
c3 = c1 | c2
print(len(c3), c3)


fs = frozenset() # нельзя использовать функции с update
print(fs, type(fs))
fs = frozenset('Hello World!')
print(fs, type(fs))

a = {1, 2, 3}
b = {3, 2, 1}
print(a == b)
