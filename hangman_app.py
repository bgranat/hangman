"""
   hangman_app.py is an app for playing hangman in the terminal
   it is also used as a module in the hangman_webapp flask app
"""

import random

def generate_random_word():
    with open('words.txt') as f: # A really hard wordlist fyi
        words = list(f)
    return random.choice(words).strip().lower()

def print_word(word, guessed_letters):
    print(dashed_word(word, guessed_letters))

def dashed_word(word, guessed_letters):
    str = ""
    for l in word.lower():
        if l in guessed_letters:
            str += l
        else:
            str += "_"
        str += " "
    return str


def play_hangman():
    want_to_play = True


    while (want_to_play):
        guessed_letters = []
        guesses_left = 6
        correct_guesses = 0
        word = generate_random_word()
        letter = input("What letter would you like to guess?\n").strip()
        done = False
        while not done:
            if letter.lower() in guessed_letters:
                guesses_left -= 1
                print("You have already guessed that letter!")
            elif letter.lower() not in word:
                guessed_letters.append(letter)
                print(f"{letter} is not in the word.")
                guesses_left -= 1
            else:
                guessed_letters.append(letter)
                correct_guesses += 1
                print(f"{letter} is in the word.")
            if correct_guesses == len(set(word)):
                done = True
                print("You won!")
            elif guesses_left == 0:
                done = True
                print(f"You lost! - The word was: {word}.")
            else:
                print_word(word, guessed_letters)
                letter = input("What letter would you like to guess?\n")
        while(True):
            replay = input("Would you like to play again? Type yes if so - no if not.\n")
            if replay.lower() == 'yes':
                want_to_play = True
                break
            elif replay.lower() == 'no':
                want_to_play = False
                break
            print("Unknown input.")

if __name__ == '__main__':
    play_hangman()
