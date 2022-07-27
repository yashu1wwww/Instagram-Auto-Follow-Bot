print()

programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
    1999: "Number type key and value pair"
}

print(programming_dictionary)
print(programming_dictionary['Bug'])
print(programming_dictionary[1999])

# add new item to dictionary
programming_dictionary["NewItem"] = "This is new item added to dictionary"
print(programming_dictionary)

# empty dictionary
empty_dictionary = {}
print(empty_dictionary)

# # wipe dictionary
# programming_dictionary = {}
# print(programming_dictionary)

# edit existing item in dictionary
programming_dictionary["Bug"] = "Updated BUG value"
print(programming_dictionary["Bug"])

print()

# dictionary loop
for key in programming_dictionary:
    # print(key)
    # print(programming_dictionary[key])

    print(f"{key} : {programming_dictionary[key]}")


"""
    nesting list and dictionary
"""

travel = {
    "India": ["Delhi", "Bangalore", "Mumbai", "Jammu"],
    "Nepal": ["Pokhra", "Himalaya"]
}

travel_1 = {
    "India": {"Citi_visited": ["Delhi", "Bangalore", "Mumbai", "Jammu"], "total_visit": 4},
    "Nepal": ["Pokhra", "Himalaya"]
}


travel_2 = [
    {
        "Country": "India",
        "Citi_visited": ["Delhi", "Bangalore", "Mumbai", "Jammu"],
        "total_visit": 4
    },
    {
        "Country": "Nepal",
        "visited_city": ["Pokhra", "Himalaya"],
        "total_visit": 2
    }
]



















