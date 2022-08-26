"""
        Old method

file = open("text.txt")
print(file.read())
file.close()

"""


# READ FILE
with open("text.txt") as file:
    a = file.read()


# # WRITE EXISTING FILE ( REMOVE ALL OLD CONTENT )
# with open("text.txt", mode="w") as file:
#     file.write("New Content")


# ADD NEW CONTENT TO EXISTING FILE
with open("text.txt", mode="a") as file:
    file.write("\nNew Content")


# CREATE NEW FILE IF FILE DOESN'T EXISTE
with open("a.txt", mode="w") as file:
    file.write("New File Added")


# A:\100 Days of Code\24 - Day\hello.py
with open("C:/Users/91800/Desktop/b.txt") as file:
    print(file.read())
















