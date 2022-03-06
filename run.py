import random
import string
import os
words = "jemoeder", "jevader"
width = os.get_terminal_size().columns

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

def menu():
    print("Play game".center(width))
    print("How to play".center(width))

    while True:
        user_input = input("Press P to play game or H for How to play".center(width)).upper()

        if user_input == "P" :
            clearscreen()
            game()
        elif user_input == "H" :
            "code comes later"
        else:
            clearscreen()
            print("invalid charachter, Please try again\n".center(width))



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
        print(f"You have {lives} lives left".center(width))
        print(f"You have used these letters:".center(width), " ".join(used_letters))
        word_list = [letter if letter in used_letters else "-" for letter in word]
        print(" ".join(word_list).center(width))

        user_letter = input("Guess a letter:\n".center(width)).upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                clearscreen()
                print(f"{user_letter} is in the word !!\n".center(width))       
            else:
                lives -= 1
                clearscreen()
                print(f"{user_letter} is not in the word\n".center(width))        

        elif user_letter in used_letters:
            clearscreen()
            print(f"You have already used {user_letter} , Please try again\n".center(width))
        
        else:
            clearscreen()
            print("Invalid charachter, Please try again\n".center(width))    

    if lives == 0:
        clearscreen()
        print(f"You died, the word was {word}\n".center(width))
    else:
        clearscreen()
        print(f"You guessed the word {word} !!\n".center(width))

def restart():
    while True: 
        a = input("Do you want to play again? Y/N\n".center(width)).upper()
        
        if a == "Y":
            clearscreen()
            game()
        elif a == "N":
            clearscreen()
            print("Thank you for playing hangman, see you later!\n".center(width))
        else:
            clearscreen()
            print("Invalid choise, please chose again\n".center(width))









def main():
    """
    run all program function
    """
    random_word(words)
    menu()
    game()
    restart()

    
main()
