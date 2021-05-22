# from datetime import datetime


# *args, **kwargs
def time_measure(args_decor):
    print(args_decor)

    def outer(func):
        def wrapper(*args, **kwargs):
            from datetime import datetime
            start = datetime.now()
            result = func(*args, **kwargs)
            print(datetime.now() - start)
            return result
        return wrapper
    return outer


@time_measure('GEN_1')
def gen_1(num):
    lst = []
    # start = datetime.now()
    for i in range(num):
        if i % 2:
            lst.append(i)
    # print(datetime.now() - start)
    return lst


@time_measure('GEN_2')
def gen_2(num):
    # start = datetime.now()
    lst = [i for i in range(num) if i % 2]
    # print(datetime.now() - start)
    return lst


print(len(gen_1(10**7)))
print(len(gen_2(10**7)))


def func(*args):
    print(type(args), args)


func()
func(1)
func(1, 2, 3, 4, 5)

# (1) <=> (1,)
# 1    1,


def func_1(**kwargs):
    print(type(kwargs), kwargs)


func_1(r=4, y=8, er='4576456')
