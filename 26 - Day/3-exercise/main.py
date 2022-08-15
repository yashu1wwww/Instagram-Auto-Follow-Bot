with open("file1.txt") as file1:
    file1_numbers = file1.readlines()

with open("file2.txt") as file2:
    file2_numbers = file2.readlines()

result = [int(number) for number in file1_numbers if number in file2_numbers]

print(result)




"""
        MY SOLUTION

with open("file1.txt") as file1:
    f1 = file1.readlines()
    file1_numbers = [int(number.strip()) for number in f1]

with open("file2.txt") as file2:
    f2 = file2.readlines()
    file2_numbers = [int(number.strip()) for number in f2]

result = [number for number in file1_numbers if number in file2_numbers]

print(result)

"""