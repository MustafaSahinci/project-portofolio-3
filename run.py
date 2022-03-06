import random
import string
import os
words = "jemoeder", "jevader"

def clearscreen(numlines=100):
    """
    Clear the console.
    numlines is an optional argument used only as a fall-back.
    """
    if os.name == "posix":
        # Unix/Linux/MacOS/BSD/etc
        os.system('clear')
    elif os.name in ("nt", "dos", "ce"):
        # DOS/Windows
        os.system('CLS')
    else:
        # Fallback for other operating systems.
        print('\n' * numlines)


def random_word(words):
    """
    choose random word
    """
    word = random.choice(words).upper()

    return word

def game():
    """
    user input and validate the input
    """
    word = random_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    lives = 6

    while len(word_letters) > 0 and lives > 0:
        print(f"You have {lives} lives left")
        print(f"You have used these letters:", " ".join(used_letters))
        word_list = [letter if letter in used_letters else "-" for letter in word]
        print(" ".join(word_list))

        user_letter = input("Guess a letter:\n").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                clearscreen()
                print(f"{user_letter} is in the word !!\n")            
            else:
                lives -= 1
                clearscreen()
                print(f"{user_letter} is not in the word\n")          

        elif user_letter in used_letters:
            clearscreen()
            print(f"You have already used {user_letter} , Please try again\n")
        
        else:
            clearscreen()
            print("Invalid charachter, Please try again\n")     

    if lives == 0:
        clearscreen()
        print(f"You died, the word was {word}")
    else:
        clearscreen()
        print(f"You guessed the word {word} !!")








def main():
    """
    run all program function
    """
    random_word(words)
    game()
    

main()
