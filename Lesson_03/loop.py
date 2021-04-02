"""
while <condition>:
    operator 1
    operator 2
    operator 3

operator 4 - не в цикле

"""
a = 1
while a <= 10:
    print(a, end=' ')
    a += 1

print()

"""
for var in <iterable_object>:
    operator 1
    operator 2
    operator 3
    
for _ in <iterable_object>:
    operator 1
    operator 2
    operator 3
"""

#  for s in '1 2 3 4 5 6 7 8 9 10':  # .split():
#  print(s, end=' ')

# range(start, stop, step)
# range(start, stop) default step = 1
# range(stop) default start = 0 and step = 1

var = 2
for var in range(2, 11, var):
    print(var, end=' ')
print()
v = 0
for v in range(20):
    print(v, end=' ')
print()

s = 'Process finished with exit code 0'
for v in s:
    if v != ' ':
        print(v, end=' ')
    else:
        break
print()

#  continue

s = 'Process finished with exit code 0'
for v in s:
    if v == ' ':
        continue

    print(v, end=' ')

print()

s = 'Process finished with exit code 0'
for v in s:
    if v != ' ':
        print(v, end=' ')
    else:
        break  # если выполняеться, то else не выполняется
else:  # выполняеться при выполнении if
    print(' end')
print()

num = 0
while True:
    num = int(input())
    if num == 0:
        break
