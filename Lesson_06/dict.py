
dic = {}
dic = dict()

"""
    d = {
        key1: value1,
        key2: value2,
        key3: value3
    }
"""

dic = dict(
    [
        (1, 'one'),
        (0, 'zero'),
        (4, 'four')
    ]
)
print(dic)

d = {
    1: 'one',
    0: 'zero',
    4: 'four'
}
print(d)

d = dict(
    one=1,
    zero=0,
    four=4,
    two=2
)

print(d)

for el in d:
    print(el, end=' ')
    print(d[el], end=' ')
    d[el] += 5
    print(d[el])

# d = {
#     [1, 2]: 'rever'
# }
# print(d)

person = {}
person['name'] = 'Peter'
print(person)
person['name'] = 'Ivan'
print(person)
person['age'] = 24
person['children'] = ['Alex', 'Olga', 'Sergey']
print(person)
person['pets'] = {'cat': 'Fox', 'dog': 'Pluto'}
print(person)
print(person['name'])
print(person['children'][1])
print(person['pets']['dog'])

d = {
    0: 'str1',
    1: 'str2',
    3: 3,
    4: 5,
    5: True
}

print(d[1])
print(d[3])
# print(d[2])

# len()
print(len(person))

# dict.clear()
# person.clear()
# print(person)

# dict[key]
print(person['name'])
# print(person['surname'])

# dict.get(key, default_value)
print(person.get('name', 'no name'))
print(person.get('surname', 'no name'))

# dict.pop(key)
res = person.pop('children')
print(res)
print(person)

# dict.popitem()
key, value = person.popitem()
print(key, value)
print(person)

# dict.update(dict1)
d1 = {'a': 10, 'b': 20, 'c': 30}
d2 = {'b':200, 'd': 300}
print(d1, d2)
d1.update(d2)
print(d1, d2)

# dict.keys()
# dict.values()
# dict.items()
key = d1.keys()
print(type(key), key)
values = d1.values()
print(type(values), values)
item = d1.items()
print(type(item), item)

for key, values in d1.items():
    print(key, '-->', values)

lst = [1, 2, 3, 4, 5]
dic = dict.fromkeys(lst)
print(dic)

