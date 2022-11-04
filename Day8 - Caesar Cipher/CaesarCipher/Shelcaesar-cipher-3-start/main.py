alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar(). 

def caesar(plain_text, shift_amount,direction_choice):
    changed_text = ""
    for letter in plain_text:
        position = alphabet.index(letter)
        if direction_choice == "encode":
            new_position = position + shift_amount
            changed_text += alphabet[new_position]
        elif direction_choice == "decode":
            new_position = position - shift_amount
            changed_text += alphabet[new_position]
    print(f"The {direction_choice}d text is {changed_text}")    
    
caesar(plain_text=text,shift_amount=shift,direction_choice=direction)


#TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.