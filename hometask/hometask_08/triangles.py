height = int(input("Введите высоту треугольника: "))
width = height * 2 - 1


# A
for i in range(height):
    # print(i, end='\t')
    for j in range(width):
        if j == width // 2 + i or i == height - j - 1 or i == height - 1:
            print('*  ', end='')
        else:
            print('   ', end='')
    print()
print()


# B
for i in range(height):
    # print(i, end='\t')
    for j in range(width):
        if width // 2 + i >= j >= width // 2 - i or i == height - 1:
            print('*  ', end='')
        else:
            print('   ', end='')
    print()
print()


# C
for i in range(0, height//2 + 1):
    # print(i, end='\t')
    for j in range(width):
        if width // 2 + i >= j >= width // 2 - i or i == height - 1:
            print('*  ', end='')
        else:
            print('   ', end='')
    print()
for i in range(height//2 + 1, height):
    for j in range(width):
        if j == i or j == height - i + width//2 - 1:
            print('*  ', end='')
        else:
            print('   ', end='')
    print()
print()


# D
for i in range(0, height//2 + 1):
    # print(i, end='\t')
    for j in range(width):
        if width // 2 + i >= j >= width // 2 - i or i == height - 1:
            print('*  ', end='')
        else:
            print('   ', end='')
    print()
for i in range(height//2 + 1, height):
    for j in range(width):
        if j == i or j == width//2 or j == height - i + width//2 - 1:
            print('*  ', end='')
        else:
            print('   ', end='')
    print()
print()
