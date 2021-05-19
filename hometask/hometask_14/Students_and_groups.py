"""
Создать класс, описывающий группу студентов - `Group`. Данный класс хранит студентов в виде списка объектов `Student`
также реализованного в виде соответствующего класса.

В классах реализовать необходимый набор атрибутов (Например класс `Student` должен иметь атрибуты `name`, `surname`,
`grades`), а так же необходимый набор методов экземпляра для работы с этими экземплярами.

Наследование здесь не понадобится.
"""


class Group:
    def __init__(self, name):
        self.__name = name
        self.__students = []

    def add_students(self, students):
        for student in students:
            self.__students.append(student)

    def del_students(self, students):
        for student in students:
            return self.__students.remove(student)

    def __str__(self):
        return "Group: {g}:\n   {student_name}".format(
            g=self.__name,
            student_name='\n   '.join(str(s) for s in self.__students)
        )


class Student:
    def __init__(self, name, surname):
        self.__name = name
        self.__surname = surname
        self.__grades = []

    def set_grades(self, grades):
        self.__grades = grades

    def add_grade(self, grade):
        self.__grades.append(grade)

    def get_name(self):
        return self.__name

    def get_surname(self):
        return self.__surname

    def __str__(self):
        return "Name: {n}, Surname: {s}, Grades: {g}".format(
            n=self.__name,
            s=self.__surname,
            g=", ".join(str(g) for g in self.__grades)
        )


student_1 = Student("Bob", "Brown")
lst = [8, 10, 9, 7, 6, 5]
student_1.set_grades(lst)
student_1.add_grade(5)
print(student_1)

student_2 = Student("Carl", "Jonson")
lst_2 = [10, 8, 6, 5, 7, 6]
student_2.set_grades(lst_2)
student_2.add_grade(12)
print(student_2)

student_3 = Student("Peter", "Parker")
lst_3 = [12, 9, 5, 8, 10, 8]
student_3.set_grades(lst_3)
student_3.add_grade(7)
print(student_3)
print()

group = Group("№1")
group.add_students([str(student_1.get_name()) + " " + str(student_1.get_surname()),
                    str(student_2.get_name()) + " " + str(student_2.get_surname()),
                    str(student_3.get_name()) + " " + str(student_3.get_surname())])
print(group)
print()
group.del_students([str(student_1.get_name()) + " " + str(student_1.get_surname())])
print(group)
print()
group_2 = Group("№2")
group_2.add_students([str(student_1.get_name()) + " " + str(student_1.get_surname())])
print(group_2)
