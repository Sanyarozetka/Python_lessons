"""
Реализовать класс цифрового счетчика. В классе реализовать методы:
 - установки максимального и минимального значений (так же начального значения счётчика),
 - увеличения счетчика на 1,
 - возвращения текущего значения счётчика
"""


class DigitalCounter:
    value = 0

    def __init__(self, start=None, end=None):
        self.start = start
        self.end = end

    def update_value(self):
        if self.value < self.end:
            self.value += 1
            return self.value
        else:
            return 'Out of range'

    def print_value(self):
        return print(self.update_value())


count = DigitalCounter(start=0, end=3)
count.print_value()
count.print_value()
count.print_value()
count.print_value()
