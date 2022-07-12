alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

# Number of character hops to be performed while ciphering a message
num_step = 3

# Cipher a string using the number of character steps provided above
def cipher(message):
    cipher = ""
    for letter in message:
        if letter.isalpha():
            letter_index = alphabet.index(str.lower(letter))
            if letter_index - num_step >= 0:
                shifted_index = letter_index - num_step
                cipher += alphabet[shifted_index]
            else:
                new_step = (letter_index - num_step) * -1
                shifted_index = len(alphabet) - new_step
                cipher += alphabet[shifted_index]

    return cipher

# Deciphers a ciphered string using the number of character steps provided above
def decipher(cipher):
    message = ""
    for letter in cipher:
        letter_index = alphabet.index(str.lower(letter))
        if letter_index + num_step > len(alphabet) - 1:
            deciphered_index = ((letter_index + num_step) - len(alphabet))
            message += alphabet[deciphered_index]
        else:
            deciphered_index = letter_index + num_step
            message += alphabet[deciphered_index]

    return message