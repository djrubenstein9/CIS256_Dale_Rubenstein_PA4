# Dale Rubenstein
# CIS256 Fall 2026
# Programming Assignment 4.guess_the_word

import random

"""
Function using random to pick one of the words in the list.
"""
def chosen_word(words):
    return random.choice(words)


def show_secret(secret_word, guessed_letters):
    for letter in secret_word:
        if letter in guessed_letters:
            print(f"{letter}", end = '')
        else:  
            print(" _ ", end='')         
    print("\n")


def user_guess(guess, secret_word):
    if len(guess) > 1 or not guess.isalpha():
        raise ValueError("Single letters only please.") 
    else:
        if guess in secret_word:
            return True
        else:
            return False


def get_the_letters(word):
    current_word = "".join(set(word))
    return current_word    


words = ['DRACULA', 'VANHELSING', 'MINA', 'RENFIELD', 'HARKER', 'LUCY']

attempts = 3
good_guesses = ''
bad_guesses = ''

print("Guess the word. Hint: Names from a Bram Stoker story.")

secret_word = chosen_word(words)
hidden_word = (" _ " * len(secret_word))
print(hidden_word)


while attempts > 0 and len(good_guesses) < len(get_the_letters(secret_word)):

    print(get_the_letters(secret_word))
    guess = input("Guess a letter: ").upper()

    try:
        guess_in_word = user_guess(guess, secret_word)

        if guess in secret_word:
            if guess in good_guesses:
                print(f"You already tried the letter {guess}.", end = ' ')
            else:
                print(f"Ohhh, {guess} is part of the secret word.", end =' ')
                good_guesses += guess

        elif guess not in secret_word:
            if guess in bad_guesses:
                print(f"You already tried the letter {guess}.")

            else:
                print(f"Sorry, {guess} is not a part of the word.", end = ' ')
                attempts -= 1
                bad_guesses += guess
        
        print(f"{attempts} attempts remain. Choose wisely.\n")
        show_secret(secret_word, good_guesses)


    except ValueError as e:
        print(e)

    #print(f"Num of good: {len(good_guesses)}")
    #print(f"Num of letters in word: {len(get_the_letters(secret_word))}")


if len(good_guesses) == len(get_the_letters(secret_word)):
    print("You have won.....this time.")

else:
    print(f"You have lost! Try again.")