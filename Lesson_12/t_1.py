rows = int(input('Введите высоту: '))

# cols = rows * 2 - 1
# z = 0
# for x in range(rows):
#     for y in range(cols):
#         if (x == rows - 1
#             or x + y == cols // 2
#             or x + y == cols // 2 + z
#         ):
#             print('* ', end='')
#         else:
#             print('  ', end='')
#     z += 2
#     print()
# print()
#
# z = 0
# for x in range(rows):
#     for y in range(cols):
#         if (x == rows - 1
#             or cols // 2 <= x + y <= cols // 2 + z
#         ):
#             print('* ', end='')
#         else:
#             print('  ', end='')
#     z += 2
#     print()
# print()

cols = rows
z = 0
for x in range(rows):
    for y in range(cols):
        if (
            cols // 2 <= x + y <= cols // 2 + z
            and x <= rows // 2
            or x - rows // 2 == y
            or y - rows // 2 + x == rows - 1
            and x >= rows // 2 or y == cols // 2
        ):
            print('* ', end='')
        else:
            print('  ', end='')
    z += 2
    print()
print()
