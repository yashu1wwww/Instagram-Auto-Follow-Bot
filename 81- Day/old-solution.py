morse_code = {
    "a": ".-",
    'b': '-...',
    'c': '-.-.',
    'd': '-..',
    'e': ".",
    'f': '..-.',
    'g': '--.',
    'h': '....',
    'i': '..',
    'j': '.---',
    'k': '-.-',
    'l': '.-..',
    'm': '--',
    'n': '-.',
    'o': '---',
    'p': '.--.',
    'q': '--.-',
    'r': '.-.',
    's': '...',
    't': '-',
    'u': '..-',
    'v': '...-',
    'w': '.--',
    'x': '-..-',
    'y': '-.--',
    'z': '--..',
}

morse_text = ''

print(' ----- Welcome to Morse Code Translator ----- ')

user_input = input('Please enter your text\n').lower()

for x in user_input:
    for (a, b) in morse_code.items():
        if a == x:
            morse_text += b

print(morse_text)
