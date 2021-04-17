"""
def function_name(param1, param2, ..., param_n):
    operator 1
    operator 2

    return result
"""


def calculate(x, y):
    z = x + y
    return z


def request_value_from_keyboard():
    a = int(input())
    b = int(input())
    return a, b


def food_for_animal(string):
    print(string)
    a, b = request_value_from_keyboard()
    res = calculate(a, b)
    return res


c = food_for_animal("Сколько бананов и ананасов для обезьян")
print("Всего", c, "шт.")


c = food_for_animal("Сколько жуков и червей для ежей")
print("Всего", c, "шт.")


c = food_for_animal("Сколько рыб и молюсков для выдр")
print("Всего", c, "шт.")
