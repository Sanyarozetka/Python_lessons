height = 11  # int(input("Введите высоту треугольника: "))
width = height * 2 - 1

for i in range(height):
    # print(i, end='\t')
    for j in range(width):
        if j == width // 2 + i or i == height - j - 1 or i == height - 1:
            print('*  ', end='')
        else:
            print('   ', end='')
    print()
print()
