import random

max_number = 10
secret_number = random.randrange(1, max_number + 1)
# print(secret_number)

# start with one-off guess
for i in range(3, 0, -1):
    print(i, 'goes remaining')
    guess_string = input('guess a number from 1 to ' + str(max_number) + ' inclusive: ')
    guess_integer = int(guess_string)
    if guess_integer == secret_number:
        print('You guessed correctly')
        break
    elif guess_integer > secret_number:
        print('You guessed too high')
    else:
        print('You guessed too low')

