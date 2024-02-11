"""
Word guessing game.
This program selects a random word from a word list and prompts the user to guess letters.The user has a limited number of guesses to reveal all the letters in the word.
The game displays the word as underscores for unguessed letters, reveals guessed letters,and keeps track of remaining turns. It validates user input to handle incorrect guesses.
The game ends when the user guesses the full word or runs out of turns.It prints a win/lose message and reveals the word at the end.

Notes:
    Requires connection to internet, or default word list will be used.

Author: Mathew

"""
import os
import random
import re
import requests
import time

def lettering_guess():
    """
    lettering_guess prompts the user to guess a letter, validating the input is a 
    single letter that has not already been guessed. It appends valid guesses to 
    the guessed_letters list and returns the guess in lowercase.
    """
    invalid_entry = True
    while invalid_entry:
        guess = input("Guess a letter: ")
        if guess in guessed_letters:
            print("You have already guessed that letter.")
        elif len(guess) > 1:
            print("You can only guess a single letter.")
        elif re.match(r'[^a-zA-Z]', guess):
            print("Only letters please.")
        elif isinstance(guess, float):
            print("Only letters please.")
        else:
            invalid_entry = False
            guessed_letters.append(guess)
            guess = guess.lower()
    return guess


if __name__ == '__main__':

    os.system('clear')
    print("Welcome to Word Guess \nWhere you will guess letters of a randomly selected word. \nGood luck!\n")
    time.sleep(2)
    # Grabbing a random word list and failing over if issues
    try:
        wordlist = requests.get('https://random-word-api.herokuapp.com/word?number=10').content.decode('utf-8').replace('[', '').replace(']', '').replace('"', '').split(',')
    except:
        wordlist = ['cyber', 'hacker', 'owasp', 'bounty']
    random_word = (wordlist[random.randrange(len(wordlist))])
    # Drawing out our guess
    unguessed_letters = ['_'] * len(random_word)
    turns_left = 10
    win_or_lose = False
    winning = False
    guessed_letters = []
    # Game loop
    while not win_or_lose:
        os.system('clear')
        print(f"The word is {unguessed_letters}")
        print(f"You have {turns_left} turns left to guess the word.")
        if len(guessed_letters) > 0:
            print(f"You have guessed the letters {guessed_letters}")
        guess = lettering_guess()
        letter_guessed_this_round = False
        # Looping through the word
        for letter in range(len(random_word)):
            if guess == random_word[letter]:
                print(f"You guessed the letter {guess} correctly!")
                time.sleep(1)
                unguessed_letters[letter] = guess
                letter_guessed_this_round = True
                if '_' not in unguessed_letters:
                    print("You win!")
                    win_or_lose = True
                    winning = True
        if not letter_guessed_this_round:
            print(f"You guessed the letter {guess} incorrectly, and lose a turn!")
            time.sleep(1)
            turns_left -= 1
            if turns_left == 0:
                print("You lose!")
                win_or_lose = True
    if winning:
        print(f"The word was {random_word}, and you had {turns_left} turns left.")
    else:
        print(f"The word was {random_word}, better luck next time.")