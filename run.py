import os
import random
import string

WORDS = ["apple", "banana", "avocado","blackberries","Cherry",
         "Apricots", "mango", "orange", "watermelon","Pear",
         "Strawberry", "Nectarine", "Grape", "Pomegranate",
         "Plum", "Mandarin", "Papaya", "Kiwi", "Pineapple",
         "Lime", "Lemon", "Grapefruit", "Melon", "Peach"]
width = os.get_terminal_size().columns

display_hangman = [
    """
                                     ___________
                                    | /        |
                                    |/        ( )
                                    |         /|\\
                                    |          |
                                    |         / \\
                                    |              \n""",
    """
                                     ___________
                                    | /        |
                                    |/        ( )
                                    |          |\\
                                    |          |
                                    |         / \\
                                    |              \n""",
    """
                                     ___________
                                    | /        |
                                    |/        ( )
                                    |          |
                                    |          |
                                    |         / \\
                                    |              \n""",
    """
                                     ___________
                                    | /        |
                                    |/        ( )
                                    |          |
                                    |          |
                                    |         /
                                    |              \n""",
    """
                                     ___________
                                    | /        |
                                    |/        ( )
                                    |          |
                                    |          |
                                    |
                                    |              \n""",
    """
                                     ___________
                                    | /        |
                                    |/        ( )
                                    |
                                    |
                                    |
                                    |              \n""",
    """
                                     ___________
                                    | /        |
                                    |/
                                    |
                                    |
                                    |
                                    |              \n"""
]


def clear_screen(numlines=100):
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


def random_word():
    """
    choose random word
    """
    word = random.choice(WORDS).upper()

    return word


def header():
    """
    print the header
    """
    print(
        "||  ||   //\\\   ||\\\  || ||///   ||\\\  //||"
        "   //\\\   ||\\\  ||".center(width),
        "||--||  //--\\\  || \\\ || ||  //| || \\\// ||"
        "  //--\\\  || \\\ ||".center(width),
        " ||  || //    \\\ ||  \\\|| ||||||| ||      ||"
        " //    \\\ ||  \\\||\n".center(width), sep=os.linesep
    )


def clear_header():
    """
    calls clear_screen and header functions
    """
    clear_screen()
    header()


def name_input():
    """
    the user must input his name
    """
    header()
    while True:
        name = input("Enter your name:\n".center(width))
        if not name.isalpha():
            clear_header()
            print("Name must be alphabets only\n".center(width))
        else:
            clear_screen()
            break
    return name


def menu(name):
    """
    Shows the welcome message and the choises the user can choose.
    play game and how to play
    """
    header()
    print(F"Welcome {name}\n".center(width))
    print("Play game".center(width))
    print("How to play\n".center(width))

    while True:
        user_input = input(
            "Press P to play game or H for"
            " How to play\n.".center(width)).upper()
        if user_input == "P":
            clear_screen()
            play_game(name)
        elif user_input == "H":
            clear_header()
            print(
                "Try to guess the hidden letters\n".center(width),
                "If you guess correctly, the letter will"
                " reveal itself\n".center(width),
                "If you guess incorrectly, you will lose a life\n".center(
                    width),
                "You have 6 lives\n".center(width),
                "Good Luck!\n".center(width), sep=os.linesep)
            enter_input = input(
                "press enter to go back\n".center(width)).upper()
            if enter_input == "":
                clear_screen()
                menu(name)
            else:
                clear_header()
                print("you typed some text before"
                      " pressing enter\n".center(width))
        else:
            clear_header()
            print("invalid charachter, Please try again\n".center(width))


def play_game(name):
    """
    get user input and validate the input
    if word_letters = 0, user wins
    if lives = 0, user lose
    """
    header()
    word = random_word()
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    lives = 6

    while len(word_letters) > 0 and lives > 0:
        print(f"Hello {name} you have {lives} lives left".center(width))
        print("You have used these letters:\n".center(
            width), " ".join(used_letters))
        word_list = [
            letter if letter in used_letters else "-" for letter in word]
        print(display_hangman[lives])
        print(" ".join(word_list).center(width))

        user_letter = input("Guess a letter:\n".center(width)).upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                clear_header()
                print(f"{user_letter} is in the word !!\n".center(width))
            else:
                lives -= 1
                clear_header()
                print(f"{user_letter} is not in the word\n".center(width))

        elif user_letter in used_letters:
            clear_header()
            print(
                f"You have already used {user_letter} ,"
                " Please try again\n".center(width))
        else:
            clear_header()
            print("Invalid charachter, Please try again\n".center(width))

    if lives == 0:
        clear_header()
        print(display_hangman[lives])
        print(f"Oh My God! They Killed {name}, You Bastards! the word was {word}\n".center(width))
        restart(name)
    else:
        clear_header()
        print(f"You guessed the word {word} !!\n".center(width))
        restart(name)


def restart(name):
    """
    Ask the users if they want to continue or quit
    """
    while True:
        user_input = input(
            "Would you like to continue? [Y]ES/[N]O\n".center(width)).upper()
        if user_input == "Y":
            clear_screen()
            play_game(name)
        elif user_input == "N":
            clear_screen()
            menu(name)
        else:
            clear_header()
            print("Invalid choise, please chose again\n".center(width))


def main():
    """
    run all program function
    """
    random_word()
    name = name_input()
    menu(name)


if __name__ == '__main__':
    main()
