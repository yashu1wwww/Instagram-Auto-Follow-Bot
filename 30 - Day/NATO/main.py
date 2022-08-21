import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)


"""         
        MY SOLUTION
"""

is_on = True

while is_on:
    word = input("Enter a word: ").upper()

    try:
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, Only letters in the alphabet please.")
    else:
        print(output_list)
        is_on = False


"""
        ANGELA SOLUTION

def generate():
    word = input("Enter a word: ").upper()

    try:
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, Only letters in the alphabet please.")
        generate()
    else:
        print(output_list)


generate()

"""
