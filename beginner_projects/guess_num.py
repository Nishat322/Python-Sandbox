import random

def guess(x):
    random_number = random.randint(1,x)
    guess = 0
    while guess != random_number: 
        guess = int(input(f'Guess a number between 1 and {x}: '))
        print (guess)
        if guess < random_number:
            print('Sorry, guess again you were too low')
        elif guess > random_number:
            print('Sorry, guess again you were too high')
    print('Congratulations! you were correct. The number was {random_number}')
    

#guess(10)

#the lower and upper boundary cannot be the same otherwise random with throw an error
def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c'
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        feedback = input(f'Is {guess} too high (l), too low(l), or correct (c)?').lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
    print(f'Yay! The computer guessed you number {guess}')

computer_guess(10)