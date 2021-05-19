class Mine:
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    def __get_x(self):
        return self.__x

    def __get_y(self):
        print('Getter')
        return self.__y

    def __set_x(self, value):
        self.__x = value

    def __set_y(self, value):
        print('Setter')
        self.__y = value

    def __del_x(self):
        self.__x = 0

    def __del_y(self):
        print('Deleter')
        self.__y = 0

    x = property(__get_x, __set_x, __del_x)
    y = property(__get_y, __set_y, __del_y)


m1 = Mine(4, 6)
# print(m1.get_y())
print(m1.y)
m1.y = 89
del m1.y


class Mine1:
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    @property
    def x(self):
        print('Getter X')
        return self.__x

    @x.setter
    def x(self, value):
        print('Setter X')
        self.__x = value

    @property
    def y(self):
        print('Getter')
        return self.__y

    @y.setter
    def y(self, value):
        print('Setter')
        self.__y = value


m2 = Mine1()
print(m2.x)
m2.x = 45
print(m2.x)
