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
    return "".join(set(word))

words = ['DRACULA', 'VANHELSING', 'MINA', 'RENFIELD', 'HARKER', 'LUCY']

attempts = 6
guessed_letters = ''

print("Guess the word. Hint: Names from a Bram Stoker story.")

secret_word = chosen_word(words)
print(" _ " * len(secret_word))

while attempts > 0 and len(guessed_letters) < len(get_the_letters(secret_word)):

    guess = input("Guess a letter: ").upper()

    try:
        guess_in_word = user_guess(guess, secret_word)

        if guess in secret_word:
                print(f"Ohhh, {guess} is part of the secret word.", end =' ')
        else:
            if guess in guessed_letters:
                print(f"You already tried the letter {guess}.")
            else:
                print(f"Sorry, {guess} is not a part of the word.")
            attempts -= 1

        guessed_letters += guess
        print(f"{attempts} attempts remain. Choose wisely.")
        show_secret(secret_word, guessed_letters)
        #print(secret_word)
        
        #print(f"Correct letters guessed so far: {guessed_letters}")


    except ValueError as e:
        print(e)

if len(guessed_letters) == len(get_the_letters(secret_word)):
    print("You have won.....this time.")

else:
    print(f"You have lost! Try again.")