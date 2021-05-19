class Person:
    def __init__(self, name, age):
        self.__name = name  # устанавливаем имя
        self.__age = age  # устанавливаем возраст

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age in range(1, 100):
            self.__age = age
        else:
            print("Недопустимый возраст")

    def display_info(self):
        print("Имя:", self.__name, "\tВозраст:", self.__age)


class Employee(Person):
    # определение конструктора
    def __init__(self, name, age, company):
        super().__init__(name, age)
        self.company = company

    # переопределение метода display_info
    def display_info(self):
        super().display_info()
        print("Компания:", self.company)


class Student(Person):
    # определение конструктора
    def __init__(self, name, age, university):
        Person.__init__(self, name, age)
        self.university = university

    # переопределение метода display_info
    def display_info(self):
        print("Студент", self.get_name(), "учится в университете", self.university)


people = [
    Person("Tom", 23),
    Student("Bob", 19, "Harvard"),
    Employee("Sam", 35, "Google")
]

for person in people:
    person.display_info()
    print()
