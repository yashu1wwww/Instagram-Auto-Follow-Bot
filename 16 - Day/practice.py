"""

class Hello:
    name = "Arunesh"


print(Hello.name)


c = Hello()

print(c.name)

"""


class Person:
    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

    def details(self):
        return f"Hello {self.firstname} {self.lastname}, your age is {self.age}"


p = Person("Arunesh", "kumar", 23)

# print(p.firstname)
# print(p.lastname)
# print(p.age)
#
# p.age = 20
#
# print(p.details())
#
# # del p.firstname
#
# # del p
#
# print(p.firstname)


class Person1:
    def __init__(xyz, name, age):
        xyz.name = name
        xyz.age = age

    def details(abc):
        return f"Hello {abc.name} your age is {abc.age}"


p1 = Person1("Arunesh", 23)

# print(p1.name)
# print(p1.age)
# print(p1.details())
