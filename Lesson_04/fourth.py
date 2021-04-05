"""
⚽
"""

a = 123456789123456789
print(bin(a))  # двоийчная система
print(oct(a))  # восьмиричная система
print(hex(a))  # шестнадцатиричная система

print(chr(0x26bd))
print('\u26bd')  # \u - 2      \U - 4
print(chr(9917))

print(ord('⚽'))
print(hex(ord('🚣')))

wave = '~'
boat = '0x1f6a3'
seagull = '\u033c'
# fish = '\U00001F'


string = '0Process finished with exit code '

#   -5 -2 -3 -2 -1
#    H  E  L  L  O
#    0  1  2  3  4

#  print(string[0])
# print(string[len(string)-1])
# print(string[-1])
# print(string[-40])

# str[start: stop: step]
# str[:]

s1 = 'Process finished with exit code 0'
print(s1[0])
print(s1[:11])
print(s1[12:123132])
print(s1[12:18:3])
print(s1[::-1])
print(s1[::-2])
print(s1[::2])
print(s1[1::2])

s = 'Process finished with exit code 0'
# len(str)
print(len(s))

# find(sub, start, end)
# rfind(sub, start, end)
print(s.find('it'))

# replace(old, new, count)
s2 = s.replace('e', 'E', 4)
print(s2)

# count(sub, start, end)

print(s.count('e', 0, 8))

# capitalize()
s = 'finishEd wiTh exit cOde 0'
print(s.capitalize())

# upper()
# lower()
s3 = s.upper()
print(s3)
print(s3.lower())

# strip(sub)
s = '     aaaaaaaaaaafinishEd wiTh exit cOde 0bbbbbbbbbb         '
print('(' + s + ')')
s4 = s.strip()
print('(' + s.strip() + ')')
s5 = s4.strip('a')
print('(' + s5 + ')')
s6 = s5.strip('b')
print('(' + s6 + ')')

# title - только с буквами
print(s.title())
