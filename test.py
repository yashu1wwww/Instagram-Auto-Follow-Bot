class Person:
    def __init__(self):
        self.firstname = "Arunesh"
        self.lastname = "kumar"

    def fullname(self):
        print(f"{self.firstname} {self.lastname}")


class Student(Person):
    def __init__(self):
        super().__init__()

    def details(self):
        print("He is good person")

    def fullname(self):
        super().fullname()
        print(f"This is new Method calling -> {self.firstname} {self.lastname}")


student = Student()
student.details()

print()
student.fullname()
print()

print(student.firstname)
