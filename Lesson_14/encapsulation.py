class Computer:
    def __init__(self, cpu, memory, hdd):
        self.__cpu = cpu
        self._memory = memory
        self.hdd = hdd

    def print_comp(self):
        print('CPU: {}\nMemory: {}\nHDD: {}'.format(
            self.__cpu,
            self._memory,
            self.hdd
        ))


comp = Computer(2700, 16000, 3000)
print(dir(comp))

print(comp._Computer__cpu)
print(comp._memory)
print(comp.hdd)
