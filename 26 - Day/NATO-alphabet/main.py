import pandas


nato_data = pandas.read_csv("nato_phonetic_alphabet.csv")
print(nato_data)


# TODO 1. Create a dictionary in this format:
nato_dict = {row.letter: row.code for (index, row) in nato_data.iterrows()}


# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user = input("Enter a word: ").upper()


result = [nato_dict[word] for word in user]
print(result)


# user = input("Enter a word: ")
#
# result = []
#
# for char in user.upper():
#     for (index, row) in nato_data.iterrows():
#         if row.letter == char:
#             result.append(row.code)
#
# print(result)
