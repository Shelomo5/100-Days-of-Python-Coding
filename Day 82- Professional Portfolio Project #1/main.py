#  text-based (command line) program that takes any String input and converts it into Morse Code.

# Dictionary with key value pairs converting text characters into morse code characters
CHAR_MORSE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-', ' ': '/'}

# Asking user what he would like translated
user_input = input("Please type text you would like translated to Morse code: ")

# Creating list to append Morse chars
converted_to_morse = []

# Function converting to Morse chars and appending to list
def user_text_to_morse():
    for char in user_input:
        char = char.upper()
        converted_to_morse.append(CHAR_MORSE_DICT[char])
    # print(converted_to_morse)

# Calling function
user_text_to_morse()

# Converting list to a string of morse code
morse_output = ''.join(converted_to_morse)
print(f"The translation of '{user_input}' in morse code is: {morse_output} ")