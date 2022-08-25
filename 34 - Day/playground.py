"""
        TYPE - HINT
"""

age: int
name: str
is_human: bool
salary: float

age = 23
# age = "hello"
print(age)

name = "Arunesh"
# name = 44
print(name)


def dl_check(driver_age: int) -> bool:
    if driver_age >= 18:
        can_drive = True
    else:
        can_drive = False
    return can_drive


if dl_check(23):
    print("You can drive")
else:
    print("Sorry, You can't drive")


















