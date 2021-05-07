
# res = 0
# try:
#     a = int(input('Please enter first number: '))
#     b = int(input('Please enter second number: '))
#     res = a / b
# # except Exception as ex:
# #     print('Exception')
# except ZeroDivisionError as ex:
#     print('ZeroDivisionError', ex)
# except ValueError as ex:
#     print('ValueError', ex)
# else:
#     print('Block ELSE')
# finally:
#     print('Block FINALLY')
#
# print(res)


# def func(value):
#     """
#
#     :param value:
#     :return:
#     """
#     if value >= 0:
#         print('Ok')
#     else:
#         raise ValueError(str(value) + ': is not correct!')
#
#
# try:
#     func(-56)
# except ValueError as ex:
#     pass

a = 8
b = 0

assert (b != 0, "Some message")

if b != 0:
    res = a / b
    print(res)
