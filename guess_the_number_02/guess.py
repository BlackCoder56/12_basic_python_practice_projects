import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0    
    while guess != random_number:
        guess = int(input(f'Guess number between 1 and {x}: '))
        if guess > random_number:
            print('The guessed number is higher than random number')
        elif guess < random_number:
            print('The guessed number is lower than random number')    
    print(f'You guess the {random_number} corrently, yeay!')
    
guess(100)
        