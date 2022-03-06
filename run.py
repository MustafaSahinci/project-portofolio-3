import random
import string
words = "jemoeder", "jevader"
lives = 6

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

    while len(word_letters) > 0 :
        print(f"you have used these letters:", " ".join(used_letters))
        word_list = [letter if letter in used_letters else "-" for letter in word]
        print(" ".join(word_list))

        user_letter = input("Guess a letter:\n").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)

        elif user_letter in used_letters:
            print("You have already used that letter, Please try again")

        else:
            print("invalid charachter, Please try again")







def main():
    """
    run all program function
    """
    random_word(words)
    game()
    

main()
