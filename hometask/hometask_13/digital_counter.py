"""
Реализовать класс цифрового счетчика. В классе реализовать методы:
 - установки максимального и минимального значений (так же начального значения счётчика),
 - увеличения счетчика на 1,
 - возвращения текущего значения счётчика
"""


class DigitalCounter:
    def __init__(self, start, end, value=None):
        self.start = start
        self.end = end
        if value is None:
            self.value = self.start
        else:
            self.value = value

    def update_value(self):
        if self.value < self.end:
            self.value += 1
        else:
            self.value = self.start

    def return_value(self):
        return self.value

    def __str__(self):
        return 'Current value: {}'.format(self.value)


count = DigitalCounter(0, 10)
for _ in range(15):
    print(count)
    count.update_value()
