import random
from words import words
import string

# getting valid word
# getting word with no spaces or dash[-]
def get_valid_word(words):
    word = random.choice(words) # gets initial random word
    while '-' in word or ' ' in word: # iterates whenever the word contains dash[-] or space
        word = random.choice(words) # gets new random number    
    return word # returns valid word

# hangman function
def hangman():
    word = get_valid_word(words) # getting valid word
    word_letter = set(word) # storing valid word in set
    alphabet = set(string.ascii_uppercase) # dictionary alphabets
    used_letter = set() # letters user already guessed   
    lives = 6 
    
    while len(word_letter) > 0 and lives > 0:        
        
        print('Used letters: ', ' '.join(used_letter)) # print used letters
        
        word_list = [letter if letter in used_letter else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))  # print currently guessed word 
        print('--------------------------------------')
        print('\nYou remaining with ', lives, ' lives') # print lives remaining
        
        # user input
        user_letter = input('Guess the word: ').upper()       
        print('--------------------------------------\n')
        if user_letter in alphabet - used_letter: # validatin if user_letter is a valid alphabet and is not in used_letter
            used_letter.add(user_letter)
            if user_letter in word_letter:
                word_letter.remove(user_letter)        
            else:
                lives = lives - 1    
        elif user_letter in used_letter:
            print('\nYou have already used this character!!')
        else:
            print('\nInvalid input!')
    # when word letter == 0
    if lives == 0:
        print('You failed to guess ', word, ' right.')
    else:
        print('You have guessed the word ', word, ' right. Yay!!\n')
    

# Calling the hangman() function
hangman() 