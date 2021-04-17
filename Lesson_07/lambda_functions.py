import random

# def fahrenheit(temperature):
#     return round(((float(9)/5) * temperature + 32), 2)
#
#
# def celsius(temperature):
#     return round((float(5)/9)*(temperature - 32), 2)


temperatures = (36.5, 37, 37.5, 38, 39)

# lst = []
# for t in temperatures:
#     lst.append(fahrenheit(t))

# print(lst)

#     lambda x, f, r: x + f * r

# m = tuple(map(fahrenheit, temperatures))
# print(m, type(m))
#
# c = tuple(map(celsius, m))
# print(c)

m = tuple(map(lambda t: round(((float(9)/5) * t + 32), 2), temperatures))
print(m, type(m))

c = tuple(map(lambda t: round((float(5)/9)*(t - 32), 2), m))
print(c)

# filter
lst1 = [random.randint(10, 99) for _ in range(30)]
print(lst1)

lst2 = list(filter(lambda x: x % 2, lst1))
print(lst2)

lst3 = list(filter(lambda x: not x % 2, lst1))
print(lst3)
