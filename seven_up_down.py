import random

print ('Let\'s play Seven Up Seven Down game.')
print ('Guess the sum of values rolled on 2 dices. Wheather the sum is more than 7, less than 7 or equal to 7? ')
guess = input('Enter up/down/equal : ')
dice1 = random.randint(1,6)
dice2 = random.randint(1,6)
print (f'Dice 1 value : {dice1}')
print (f'Dice 2 value : {dice2}')
if (dice1+dice2 >= 7 and guess == 'up'):
    print ('You won.')
elif (dice1+dice2 < 7 and guess == 'down'):
    print ('You won')
elif (dice1+dice2 == 7 and guess == 'equal'):
    print ('You won')
else:
    print ('You lost.')
