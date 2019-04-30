"""This is a code for the hangman game"""
from os import system, name
from time import sleep
from random import *


def clear():
    """ Function to clear the Console """
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


class Hangman:
    def __init__(self, word):
        self.word = word
        self.tries = len(word) + 1  # easy word has less tries than a big ones
        self.blank = ["- " for i in word]
    

    def SetField(self):
        clear()
        print(f"Tries Left: {self.tries}")
        print(f"Word: {''.join(self.blank)}\n")

    def GetInput(self):
        while True:
            print("Please enter your choice")
            choice = input(">>> ")

            if len(choice) == 0:
                print("String can't be zero\n\n")
                continue
            else:
                break

        correct = False

        for i in range(len(self.word)):
            if self.word[i] in choice:
                self.blank[i] = self.word[i]+" "
                correct = True

        if correct is False:
            self.tries -= 1

class Library:
    """ Library for all our Words """
    
    @staticmethod
    def GetWord(category):
        easy = [
            "dog", "cat", "spam", "rat", "python", "book",
            "snake", "fire", "computer", "browser", "fire"
        ]

        medium = [
                "firehose", "integrated", "intense", "console",
                "country", 'municipality', "antenna", "thorax"
        ]

        hard = [
                "encyclopedia", "administrator", "conciousness",
                "interesting", "complication"
        ]

        insane = [
                "antidisestablishmentarianism", "floccinaucinihilipilification",
                "pneumonoultramicroscopicsilicovolcanoconiosis"
        ]
        
        if category == "e":
            return easy[randint(0, len(easy)-1)]
        elif category == "m":
            return medium[randint(0, len(medium)-1)]
        elif category == "h":
            return hard[randint(0, len(hard)-1)]
        elif category == "insane":
            return insane[randint(0, len(insane)-1)]
        else:
            raise Exception("This category does not exist")



if __name__ == "__main__":
    # create class objects
    hangman = Hangman(Library.GetWord(input("Which category? (e, m, h, insane)\n: ")))
    
    # main game Loop
    while True:
        if  (''.join(hangman.blank)).replace(" ", '') == hangman.word:
            print("Congratulations!!! You Won")
            break
        elif hangman.tries == 0:
            print("Oof! Looks like you lost :(")
            break        
        else:
            hangman.SetField()
            hangman.GetInput()

    print("END OF GAME")
    input("Press Enter to quit...")
            
        
