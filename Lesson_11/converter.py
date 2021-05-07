from string import ascii_uppercase


def converter(num, base):
    temp_str = '0123456789' + ascii_uppercase
    lst = []
    while num != 0:
        lst.append(temp_str[num % base])
        num //= base

    lst.reverse()
    return ''.join(lst)


print(converter(123456, 2))
