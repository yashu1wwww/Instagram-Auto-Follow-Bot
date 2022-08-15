import random


"""
        LIST COMPRESSION

# [new_item for item in list]

# normal example
numbers = [1, 2, 3, 4, 5]
new_list = [number + 1 for number in numbers]
print(new_list)


# string to list
name = "Arunesh"
letters = [letter for letter in name]
print(letters)

# range
double_number_list = [i * 2 for i in range(1, 6)]
print(double_number_list)

# conditional
names = ["Nida", "Arunesh", "Ankesh", "Mahalaxmi", "Raksha", "Neha", "Mohan"]

sort_names_1 = [name for name in names if len(name) <= 5]
print(sort_names_1)

sort_names_2 = [name.upper() for name in names if len(name) > 5]
print(sort_names_2)

"""

"""
        DICTIONARY COMPRESSION



#   {new_key: new_value for new_key in lists}
students_name = ["Sohan", "Dohan", "Pohan", "Rohan", "Mohan", "Arunesh", "Ankesh", "Ram"]
students_score = {student: random.randint(1, 100) for student in students_name}
print(students_score)


#   with condition
#   {key: value for (key, value) in items.key() if value >= 60}
passed_students = {student: score for (student, score) in students_score.items() if score >= 60}
print(passed_students)


"""


"""
        PANDAS ITERATE
        
"""

import pandas

student_dict = {
    "student": ["Sohan", "Pohan", "Dohan"],
    "score": [43, 65, 91]
}

# for (key, value) in student_dict.items():
#     # print(key)
#     print(value)


# using of pandas
student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)
print()

# for (key, value) in student_data_frame.items():
#     # print(key)
#     print(value)

for (index, row) in student_data_frame.iterrows():
    # print(index)
    # print(row)
    # print(row.student)
    # print(row.score)
    if row.student == "Pohan":
        print(row.score)










