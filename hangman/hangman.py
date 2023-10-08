import random
from words import words
import string

def get_valid_word(words):
    word = random.choice(words) # gets initial random word
    while '-' in word or ' ' in word: # iterates whenever the word contains dash[-] or space
        word = random.choice(words) # gets new random number
    
    return word # returns valid word

def hangman():
    word = get_valid_word(words) # getting valid word
    word_letter = set(word) # storing valid word in set
    alphabet = set(string.ascii_uppercase) # dictionary alphabets
    used_letter = set() # letters user already guessed