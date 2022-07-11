alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]


message = "The river of sbou is passing and berries are growing on the floor"

num_step = 8


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


def decipher(cipher, step):
    message = ""
    for letter in cipher:
        letter_index = alphabet.index(str.lower(letter))
        if letter_index + step > len(alphabet) - 1:
            deciphered_index = ((letter_index + step) - len(alphabet))
            message += alphabet[deciphered_index]
        else:
            deciphered_index = letter_index + step
            message += alphabet[deciphered_index]

    return message


ciphered_message = cipher(message)

print("Ciphered message", ciphered_message)

deciphered = decipher(ciphered_message, num_step)

print("Deciphered message", deciphered)