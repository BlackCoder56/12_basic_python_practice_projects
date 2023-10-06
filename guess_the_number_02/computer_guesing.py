import random

def robot_guess(x):
    low = 1
    high = x
    feedback  = ''
    while feedback != 'c':
        if low != high:            
            guess = int(random.randint(low, high))
        else:
            guess = low
        feedback = input(f'\nIs {guess} too high [h], too low [L] or correct [c]: ').lower()
        if feedback == 'l':
            low = guess+1
        elif feedback == 'h':
            high = guess-1
    
    print(f'\nYay, you guessed {guess} right!!\n')
    
    
robot_guess(10)
        