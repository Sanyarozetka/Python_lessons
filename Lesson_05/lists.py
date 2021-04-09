lst = []
print(lst, type(lst))
lst = list("Hello World!")
print(lst)

lst = [1, 4.5, 'test', True, [4, 6, 'g']]
print(lst)
print(lst[2])
lst[2] = 4444
print(lst)

lst1 = [1, 2, 3]
lst2 = [4, 5, 6]
lst3 = lst1 + lst2
print(lst3)

lst3 = lst1 * 3
print(lst3)

for elem in lst3:
    print(elem, end=' ')
print()

for i in range(len(lst)):
    print(lst3[i], end=' ')
print()

# len(list)
print(len(lst3))

# A in list
# A not in list
print(3 in lst3)
print(4 in lst3)
print(3 not in lst3)
print(4 not in lst3)

# min, max, sum
print(min(lst3))
print(max(lst3))
print(sum(lst3))

# list.index(x)
print(lst3.index(3, 4))

# list.count(value)
print(lst3.count(3))
print(lst3.count(0))

# list.pop()
# list.pop(index)
print(lst3)
print(lst3.pop(4))
print(lst3)

# list.append(value)
lst3.append(555)
print(lst3)

# list.insert(index, value)
lst3.insert(3, 45)
print(lst3)

# list.clear()
# lst3.clear()
print(lst3)

# list.copy()
print(id(lst3), lst3)
lst4 = lst3
print(id(lst4), lst4)
lst4 = lst3.copy()
print(id(lst3), lst3)
print(id(lst4), lst4)
lst3[5] = 888
print(lst4)
print(lst3)

lst4 = lst3[:]

# list1.extend(list2)
# list1 + list2
print(lst1, lst2)
lst1.extend(lst2)
print(lst1, lst2)

# list.remove(value)
# del elem

print(lst3)
lst3.remove(45)
print(lst3)
del lst3[2]
print(lst3)
# del lst3
# print(lst3)

# list.reverse()

print(id(lst3), lst3)
lst3.reverse()
print(id(lst3), lst3)
lst4 = lst3[:: -1]
print(id(lst4), lst4)

# list.sort()
lst3.sort(reverse=True)
print(lst3)
