import random
from random import randint

def Get_Word():
    # world_list[0]
    word_list = ("encyclopedia", "hello world", "spam", "eggs", "Guido", "Rossum", "foux pax")
    #random number
    choice = random.randint(0, len(word_list))
    #get the word
    word = word_list[choice - 1]
    return word, word_list

def Blank_Word(word):
    blank_word = ""
    for char in range(len(word)):
        if word[char].isalpha():
            blank_word += "-"
        else:
            blank_word += word[char]
    return blank_word

def Game_Time(word, blank_word):
    tries = 6
    while True:
        input_char = input("Enter a Letter: ")
        word = list(word)
        blank_word = list(blank_word)

        for char in range(len(blank_word)):
            if input_char == word[char]:
                blank_word[char] = input_char
                break
            elif word[char] == " ":
                continue
            elif tries == 0:
                            print(f"""Aw Shucks! Your tries are up!
The Correct word was: {"".join(word)}

Better luck next time!""")
                            break
            else:
                tries -= 1
                print(f"{tries} left")
                break

        print("".join(blank_word))

        if blank_word == word:
            print("Congratulations!!!")
            input("Press Any Key to continue...")
            return
            
word = Get_Word()
blank_word = Blank_Word(word[0])
Game_Time(word[0], blank_word)
