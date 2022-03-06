import random
import string
words = "jemoeder", "jevader"

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
                print("")

            else:
                lives -= 1
                print("Letter is not in the word\n")

        elif user_letter in used_letters:
            print("You have already used that letter, Please try again\n")

        else:
            print("Invalid charachter, Please try again\n")

    if lives == 0:
        print(f"You died, the word was {word}")
    else:
        print(f"You guessed the word {word} !!")







def main():
    """
    run all program function
    """
    random_word(words)
    game()
    

main()
