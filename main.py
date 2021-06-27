import random

target_num = random.randint(1, 101)

def run_guess(trial):
    global target_num
    while int(trial) != 0:
        guess = int(input('Enter a number -->'))
        if guess > target_num:
            print('Guessed number is too high!!')
            trial -=1
            print(f'You have {trial} trials left!!')
        elif guess < target_num:
            print('Guessed number is too low!!')
            trial -=1
            print(f'You have {trial} trials left!!')
        else:
            print('You Guessed the correct number, You win 😀')
            break
    else:
        print('You ran out of time, and didn\'t guess the correct number 😣')

def diff_level(level):
    if level.lower() == 'easy':
        trial = 10
        run_guess(trial)
    elif level.lower() == 'hard':
        trial = 5
        run_guess(trial)
    else:
        print('Invalid Input..')

print(target_num) # This is to tell me what to guess towards as to keep track while coding..
print('Welcome To Fredintek Guessing Game 😁')
print('Guess a number between 1 and 100')
level = input('Choose a difficulty level.. Type "Easy or Hard"\n-->').lower()
diff_level(level)


