ALPHABETS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

MORSE_CODE = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--', '-.', '---', '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..']


def text_to_morse_code():
    text = input("Enter your text\n").lower()
    morse_text = ''

    for i in text:
        if i == ' ':
            pass
        else:
            text_index = ALPHABETS.index(i)
            morse_text += MORSE_CODE[text_index]

    print(morse_text)


start = True

while start:
    text_to_morse_code()
    user = input("Do you covert again 'text to morse code' type y\n")
    if user == "n":
        start = False
    else:
        pass
