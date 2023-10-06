import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0    
    while guess != random_number:
        
        try:            
            guess = int(input(f'\nGuess number between 1 and {x}: '))
            if guess > random_number:
                print('The guessed number is higher than random number\n')
            elif guess < random_number:
                print('The guessed number is lower than random number\n')   
        except(ValueError):
            print('Error, please try again!')
    print(f'\nYou guessed the {random_number} corrently, yeay!\n')
    
guess(100)
        