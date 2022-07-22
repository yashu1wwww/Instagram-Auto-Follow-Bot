"""
    DATA TYPE
"""
# STRING
print('Hello')
print('Hello'[0])
print('Hello'[1])
print('Hello'[-1])
print('12' + '23')

# INTEGER
print(12 + 34)
print(123_456_789)

# FLOAT
print(35.135)

# BOOLEAN
print(True)
print(False)


# STRING

print('Hello')

print('Hello'[0])
print('Hello'[1])
print('Hello'[-1])

print('12' + '23')

# Integer
print(12 + 34)
print(123_456_789)


"""
    Type Error
    Type Checking
    Type Conversion
"""

a = 242
a = "242"
print(len(a))

name_length = len(input("Enter your name ? \n"))
print(name_length)

# type check
print(type(name_length))

# type convertion
name_converte = str(name_length)

print(type(name_converte))

print("Your name length is : "+ name_converte)

print(42 + int("453"))
print(42 + float("453"))
print(42 + int("453"))
print(str(42) + "453")


"""
    Math Operator
"""

# 2+2
# 2-2
# 2*2
# 2/2
# 2**2

print(2**3)

#    PEMDAS
# ()
# **
# *
# /
# +
# -
print(3 * 3 + 3 / 3 - 3)
print(3 * (3 + 3) / 3 - 3)

"""
    Number Manipution
    F - String
"""

# NUMBER MANIPULATION
print(32.55435)
print(int(32.554246))
print(round(32.554435))
print(round(32.554, 2))

score = 10
score += 1
score -= 1
score *= 2
score /= 2
print(score)

status = "acrive"
married = True

# F - String
print(f"Score = {score}, Status = {status}, Married = {married}")
