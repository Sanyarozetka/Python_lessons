# { [field_name] [!modifier] [:specification]}
# a-z A-Z 0-9 _

"""
specification
[ [fill] align ] [sign] [#] [0] [width] [,] [.precision] [type]
"""

tmp1 = 'Static text: {} - {} = {} {!r} {}'
a = 456453
b = 346345
print(tmp1.format(a, b, a - b, 'test', '\'test\''))

coord = (3, 5)
print('X: {0[0]};  Y: {0[1]}'.format(coord))           # 'X: 3;  Y: 5'
print("repr() shows quotes: {!r}; str() doesn't: {!s}".format('test1', 'test2'))
# "repr() shows quotes: 'test1'; str() doesn't: test2"
print('{:<30}'.format('left aligned'))                 # 'left aligned                  '
print('{:>30}'.format('right aligned'))                # '                 right aligned'
print('{:^30}'.format('centered'))                     # '           centered           '
print('{:*^30}'.format(' centered '))                  # '********** centered **********'
print('{:+f}; "{:=010.2f}"'.format(3.14, -34.14))              # '+3.140000; -3.140000'
print('{: f}; {: f}'.format(3.14, -3.14))              # ' 3.140000; -3.140000'
print('{:-f}; {:-f}'.format(3.14, -3.14))              # '3.140000; -3.140000'
print("int: {0:d};  hex: {0:x};  oct: {0:o};  bin: {0:b}".format(123456))
# 'int: 37;  hex: 25;  oct: 45;  bin: 100101'

print('int: {0:d};  hex: {0:#x};  oct: {0:#o};  bin: {0:#b}'.format(123456))
# 'int: 37;  hex: 0x25;  oct: 0o45;  bin: 0b100101'
points = 19.5
total = 22
print('Correct answers: {:.2%}'.format(points/total))     # 'Correct answers: 88.64%'

tmp = 'Some test: {a}, {b}, {c}, {a}, {c}, {b}'
print(tmp.format(
    a=5,
    b=7,
    c=9
))
