class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Student(Person):
    def __init__(self, name, age, course):
        super().__init__(name, age)
        self.course = course

    def study(self):
        print(self.name, "is studying", self.course)


std1 = Student("rizvan", 21, "BCA")

print("Name:", std1.name)
print("Age:", std1.age)
print("Course:", std1.course)

std1.study()