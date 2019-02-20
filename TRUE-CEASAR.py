"""
    This program is a Ceasar Cypher that I have programmed. It's still in the making.
    Follow the instructions given to you at runtime
    Ciao :-D
"""

import time
import math
from time import sleep

Max_Key = 26

def getInput():
    while True:
        mode = input("Do you wish to Encrypt or Decrypt a Message: ").lower()
        
        if mode in "encrypt e decrypt d".split():
            return mode
        else:
            print("Enter either 'encrypt'/'e' or 'decrypt'/'d'")

def getMessage():
    message = input("Enter a Message: ")
    return message

def getKey():
    key = 0
    while True:
        key = int(input(f"Enter the key number (1-{Max_Key}): "))
        if key >= 1 and key <= Max_Key:
            return key
        else:
            print("input was invalid: Try Again")

def translateMessage(mode, message, key):
    if mode[0] == 'd':
        key = -key
    translated = ''

    for character in message:
        if character.isalpha():
            num = ord(character)
            num += key

            if character.isupper():
                if num > ord('Z'):
                    num -= 26
                elif num < ord('A'):
                    num += 26

            elif character.islower():
                if num > ord('z'):
                    num -= 26
                elif num < ord('a'):
                    num += 26

            translated += chr(num)
        else:
            translated += character
    return translated

mode = getInput()
message = getMessage()
key = getKey()

print(f"""

Your translated text is: {translateMessage(mode, message, key)}""")

        
