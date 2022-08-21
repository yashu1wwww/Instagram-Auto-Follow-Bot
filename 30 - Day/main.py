"""
    Types of ERRORS

    1.) FileNotFoundError
    2.) KeyError
    3.) IndexError: list index out of range
    4.) TypeError
"""

#   FileNotFoundError
with open("no-file.txt") as file:
    file.read()


#   KeyError
a = {"A": "Hello", "B": "Hi"}
print(a["C"])


#   IndexError: list index out of range
a = [1, 2, 3, 4, 5]
print(a[9])


#   TypeError
a = "Hello"
print(a + 5)


try:
    file = open("a.txt")

    dic = {"Key": "Value"}
    print(dic["Kesdfy"])
except FileNotFoundError:
    file = open("a.txt", "w")
    file.write("Something")
    print("File does not exist")
except KeyError as e_mess:
    print(f"Error Message : [{e_mess}]")
else:
    file = open("a.txt")
    print(file.read())
finally:
    file.close()
    print("File closed")


"""
        Create New Error
        https://www.w3schools.com/python/python_ref_exceptions.asp
        
        1.) IndexError
        2.) KeyError
        3.) NameError
        4.) SyntaxError
        5.) TypeError
        6.) ValueError
"""

height = float(input("Enter your height"))
weight = int(input("Enter your weight"))

if height > 3:
    raise ValueError("Human height must be less than 3 meter")

bmi = weight / (height * height)

print(bmi)


raise ValueError("Value Error")

raise FileNotFoundError("File not exist")




















