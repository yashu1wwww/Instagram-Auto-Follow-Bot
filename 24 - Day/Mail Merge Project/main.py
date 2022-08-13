# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

with open("./Input/Letters/starting_letter.txt") as file:
    letter = file.read()


with open("./Input/Names/invited_names.txt") as file:
    names = file.readlines()

for name in names:
    nm = name.strip()
    x = letter.replace("[name]", nm)
    with open(f"Output/ReadyToSend/letter_for_{nm}.txt", mode="w") as send_letter:
        send_letter.write(f"{x}")