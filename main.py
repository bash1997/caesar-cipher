from replit import clear
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
from art import logo
print(logo)

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def caesar(direction, text, shift):

    text_list = list(text)
    cipher_list = []
    ciphered = ""
    decipher_list = []
    deciphered = ""
    while shift > 26:
        shift %= 26
    for i in range(0, len(text)):

        if (text_list[i] != " ") and text_list[i] in alphabet:
            for position in range(len(alphabet)):
                letter = alphabet[position]
                if (text_list[i] == letter) and (direction == 'encode'):
                    cipher_i = shift
                    cipher_i += position

                    if cipher_i >= 26:
                        cipher_i -= 26
                    cipher_list += alphabet[cipher_i]

                elif (text_list[i] == letter) and (direction == 'decode'):
                    decipher_i = position
                    decipher_i -= shift

                    if decipher_i < 0:
                        decipher_i += 26
                    decipher_list += alphabet[decipher_i] 
        if text_list[i] == "0":
            if direction == 'encode':
                cipher_list += "0"
            

            elif direction == 'decode':
                decipher_list += "0"

        elif text_list[i] not in alphabet:
            if direction == 'encode':                 
                cipher_list += text_list[i]
            elif direction == 'decode':
                decipher_list += text_list[i]

        if direction == 'encode':
            ciphered += cipher_list[i]
        if direction == 'decode':
            deciphered += decipher_list[i]

    if direction == 'encode':
        print(f"The encoded text is {ciphered}")
    elif direction == 'decode':
        print(f"The decoded text is {deciphered}")

caesar(direction, text, shift)

run_again = input("Would you like to run again? Y/N: ").lower()
and_again = True

while and_again == True:
    clear()
    print(logo)


    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(direction, text, shift)
    
    run_again = input("Would you like to run again? Y/N: ").lower()
    if run_again == 'n':
        and_again = False