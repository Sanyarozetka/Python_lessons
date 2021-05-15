from random import randint

rows = 11
cols = 10

matrix = [[randint(10, 99) for _ in range(cols)] for _ in range(rows)]

sum_cols = [0] * cols
for i in range(rows):
    sum_line = 0
    for j in range(cols):
        print('{:>4}'.format(matrix[i][j]), end='')
        sum_line += matrix[i][j]
        sum_cols[j] += matrix[i][j]
    print('{:>10}'.format(sum_line))

print()

print(''.join('{:>4}'.format(el) for el in sum_cols))

for i in range(cols-1):
    for j in range(cols-1-i):
        if sum_cols[j] > sum_cols[j+1]:
            sum_cols[j], sum_cols[j+1] = sum_cols[j+1], sum_cols[j]
            for m in range(rows):
                matrix[m][j], matrix[m][j+1] = matrix[m][j+1], matrix[m][j]

print()
for i in range(rows):
    sum_line = 0
    for j in range(cols):
        print('{:>4}'.format(matrix[i][j]), end='')
        sum_line += matrix[i][j]
    print('{:>10}'.format(sum_line))
print()
print(''.join('{:>4}'.format(el) for el in sum_cols))

for j in range(cols):
    for it in range(rows-1):
        for i in range(rows-1-it):
            if matrix[i][j] > matrix[i+1][j] if j % 2 else matrix[i][j] < matrix[i+1][j]:
                matrix[i][j], matrix[i+1][j] = matrix[i+1][j], matrix[i][j]

print()
for i in range(rows):
    sum_line = 0
    for j in range(cols):
        print('{:>4}'.format(matrix[i][j]), end='')
        sum_line += matrix[i][j]
    print('{:>10}'.format(sum_line))
print()
print(''.join('{:>4}'.format(el) for el in sum_cols))
