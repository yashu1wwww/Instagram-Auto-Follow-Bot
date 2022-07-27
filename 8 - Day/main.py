# Review:
# Create a function called greet().
# Write 3 print statements inside the function.
# Call the greet() function and run your code.


# function defining
def greet(name):
    print(f"Hello {name}")
    print(f"How are {name}?")


# function calling
greet("Arunesh")
greet("Ankesh")


# parameter vs argument
# "Arunesh" = argument
# name = paramenter

print()
print()

def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}")

# positional arguments
greet_with("Arunesh", "Gurgaon")


# keyword argument
greet_with(location="Dhaka", name="Ankesh")













