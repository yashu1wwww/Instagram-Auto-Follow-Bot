################### Scope ####################

enemies = 1


def increase_enemies():
  enemies = 2
  print(f"enemies inside function: {enemies}")


increase_enemies()
print(f"enemies outside function: {enemies}")



print()


##############################################################
#   LOCAL SCOPE
##############################################################

def first():
    x = 10
    print(x)


first()
# print(x)


##############################################################
#   GLOBAL SCOPE
##############################################################

players = 5


def second():
    print(players)


second()
print(players)


print()

if 5 > 2:
    a = 100
    print(a)

print(a)

print()

b = 0
while b < 5:
    c = "Hello"
    print(b)
    if b == 2:
        break
    b += 1


print(c)


print()

##############################################################
#   GLOBAL KEYWORD SCOPE
##############################################################

total = 1

print("Total : ", total)


# def details():
#     global total
#     total += 2
#
#     print("Total : ", total)

def details():
    print("Total : ", total)

    return total + 2


total = details()
print("Total : ", total)


##############################################################
#   CONSTANT
##############################################################

PI = 3.14
URL = "https://google.com/"


















