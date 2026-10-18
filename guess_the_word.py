import random



def chosen_word(words):
    return random.choice(words)

def show_secret(secret_word):
    print(" _ " * len(secret_word))

words = ['Dracula', 'Van Helsing', 'Mina', 'Renfield', 'Jonathan', 'Lucy']

attempts = 6
guessed_letters = ''

print("Guess the word. Hint: Names from a Bram Stoker story.")

secret_word = chosen_word(words)
show_secret(secret_word)