# Dale Rubenstein
# CIS256 Fall 2026
# Programming Assignment 4.guess_the_word

import random

"""
Function using random to pick one of the words in the list
of words.
"""
def chosen_word(words):
    return random.choice(words)


"""
The function user_guess is being passed any letter that a user
guesses and the secret word. If the guess is within the secret
word, then the function returns true, otherwise it returns false.
Error handling added so user only selects one letter at a time.
"""
def user_guess(guess, secret_word):
    if len(guess) > 1 or not guess.isalpha():
        raise ValueError("Single letters only please.") 
    else:
        if guess in secret_word:
            return True
        else:
            return False


"""
Function takes the secret word and a good letter guess as
parameters.  As the good letters are passed the function
prints the letters to output, otherwise the underscores
are returned to output.
"""
def show_secret(secret_word, guessed_letters):
    for letter in secret_word:
        if letter in guessed_letters:
            print(f"{letter}", end = '')
        else:  
            print(" _ ", end='')         
    print("\n")


"""
The secret word is passed to the function. The built-in
fucntion of set(word) takes the secret word, converts the
word to separate characters in no particular order, then joins 
the characters into a new string. The returned "current_word"
is used for comparison within the intial while loop to ensure
the number of attempts is less than the length of the current_word.
"""
def get_the_letters(word):
    current_word = "".join(set(word))
    return current_word    


#list of words
words = ['DRACULA', 'VANHELSING', 'MINA', 'RENFIELD', 'HARKER', 'LUCY']

#declaring variables
attempts = 3
good_guesses = ''
bad_guesses = ''

print("\nGuess the word. Hint: Names from a Bram Stoker story.")

#calling the function to get a random word from the list
secret_word = chosen_word(words)

#initial print out of how many hidden letters are in the word
hidden_word = (" _ " * len(secret_word))
print(hidden_word)

if __name__ == "__main__":

    #looping until user wins or loses
    while attempts > 0 and len(good_guesses) < len(get_the_letters(secret_word)):

        #user input of a letter
        guess = input("Guess a letter: ").upper()

        try:
            #calling the function to return a true if the letter is in the word
            guess_in_word = user_guess(guess, secret_word)

            if guess in secret_word:
                if guess in good_guesses:
                    print(f"You already tried the letter {guess}.", end = ' ')
                else:
                    print(f"Ohhh, {guess} is part of the secret word.", end =' ')
                    good_guesses += guess #saving all the good letter guesses

            elif guess not in secret_word:
                if guess in bad_guesses:
                    print(f"You already tried the letter {guess}.")

                else:
                    print(f"Sorry, {guess} is not a part of the word.", end = ' ')
                    attempts -= 1
                    bad_guesses += guess #saving all the bad letter guesses
            
            print(f"{attempts} attempts remain. Choose wisely.\n")

            #calling the function to output the letters in the word.
            show_secret(secret_word, good_guesses)


        except ValueError as e:
            print(e)

        #testing lengths of letters vs. words
        #print(f"Num of good: {len(good_guesses)}")
        #print(f"Num of letters in word: {len(get_the_letters(secret_word))}")

    #ending statements to let the user know if they have won or lost.
    if len(good_guesses) == len(get_the_letters(secret_word)):
        print("You have won.....this time.")

    else:
        print(f"You have lost! Try again.")