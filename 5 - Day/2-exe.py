# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

# Write your code below this row 👇

# HIGHEST SCORE
highest_score = 0

for x in student_scores:
    if x > highest_score:
        highest_score = x

print(f"Hihest score in the class : {highest_score}")

# # LOWEST SCORE
# lowest_score = None
#
# for x in student_scores:
#     if x < highest_score:
#         highest_score = x
#
# print(lowest_score)

# print(max(student_scores))
# print(min(student_scores))


# a = [1,2,5,3,7,4,9,3]
#
# heighest_value = 0
#
# for x in a:
#     if x < heighest_value:
#         heighest_value = x
#
# print(heighest_value)

