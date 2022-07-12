from cipher_functions import *

# Message to cipher
message = "The river of sbou is passing and berries are growing on the floor"

# Ciphers a message
ciphered_message = cipher(message)

print("Ciphered message => ", ciphered_message)

# Deciphers a message
deciphered = decipher(ciphered_message)

print("Deciphered message => ", deciphered)