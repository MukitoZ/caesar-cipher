alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(texter, shifter, directioner):
    caesar_text = ""
    new_alphabet = []
    counter = shifter
    while counter > 25:
        counter -= 26
    for i in alphabet:
        new_alphabet += alphabet[counter]
        if counter == 25:
            counter -= 25 
        else:
            counter += 1
    for x in texter:
        if directioner == "encode":
            if x in alphabet:
                index = alphabet.index(x)
                caesar_text += new_alphabet[index]
            else:
                caesar_text += x
        elif directioner == "decode":
            if x in alphabet:
                index = new_alphabet.index(x)
                caesar_text += alphabet[index]
            else:
                caesar_text += x
    print(f"The {directioner}d text is {caesar_text}")

from art import logo
print(logo)
program = True
while program:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    while direction != "encode" and direction != "decode":
        print("You have to type the right input.")
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(texter=text, shifter=shift, directioner=direction)
    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if restart == "no":
        print("Goodbye")
        program = False