
# 2 ^ 3 = 2 * 2 * 2
# 2 ^ 3 = 2 * 2 ^ 2                 2 * 4 = 8
#               2 * 2 ^ 1           2 * 2 = 4
#                     2 * 2 ^ 0     2 * 1 = 2
#                           1

def iteratively_pow(num, exp):
    res = 1
    while exp > 0:
        res *= num
        exp -= 1

    return res

#                   2  3
def recursive_pow(num, exp):
    # base case
    if exp == 0:
        return 1

    # recursive case
    #       2                   2    2
    return num * recursive_pow(num, exp-1)  # 4


print(iteratively_pow(2, 5))
print(recursive_pow(2, 5))


# 5! = 1 * 2 * 3 * 4 * 5
# 5! ==> 5 * 4! ==> 4 * 3! ==> 3 * 2! ==> 2 * 1! ==> 1
# 120<== 5 * 24 <== 4 * 6  <== 3 * 2  <== 2 * 1

def factorial_iteratively(num):
    res = 1
    for i in range(1, num + 1):
        res *= i

    return res


def factorial_recursive(num):
    if num == 1:
        return 1

    return num * factorial_recursive(num - 1)


print(factorial_iteratively(5))
print(factorial_recursive(5))

# 0 1 2 3 4 5 6  7  8  9 10 11
# 0 1 1 2 3 5 8 13 21 34 55 89


def fib_iter(num):
    f0 = 0
    f1 = 1
    while num > 1:
        r = f0 + f1
        f0 = f1
        f1 = r
        num -= 1

    return f1


def fib_rec(n):
    # return n if 0 <= n <= 1 else fib_rec(n-1) + fib_rec(n-2)
    if 0 <= n <= 1:
        return n

    return fib_rec(n-1) + fib_rec(n-2)


print(fib_iter(10))
print(fib_rec(10))
