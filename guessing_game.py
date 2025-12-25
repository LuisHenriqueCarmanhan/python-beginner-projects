from random import randint
# Computer "thinks" of a number between 0 and 5
computer_number = randint(0, 5)

print('-=' * 20)
print('I am thinking of a number between 0 and 5. Can you guess it?')
print('-=' * 20)

# 1. Inform the range in the input message
your_number = int(input('enter the number '))

# 2. Safety check: See if the player followed the rules
if your_number < 0 or your_number > 5:
    print("HEY! I said BETWEEN 0 AND 5.")
    print("You are NOT 'The One', Neo... You can't even follow a simple rule! ")
else:
    # Game Result
    if your_number == computer_number:
        print(f'\nUNBELIEVABLE! You guessed it: {computer_number}!')
        print('You are beginning to believe, Neo...')
    else:
        print(f'\nWRONG PILL! I thought of {computer_number}, not {your_number}.')
        print('Fate, it seems, is not without a sense of irony.')
        
print('\n' + '=' * 40)
print('    Simulation Terminated. Free your mind.    ')
print('=' * 40)