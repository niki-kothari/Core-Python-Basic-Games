import random

def check_number(compNo, guessNo):
    if (compNo == guessNo):
        return True
    elif (compNo > guessNo):
        print ('Number you guess is less than computer generated number')
        return False
    elif (compNo < guessNo):
        print ('Number you guess is greater than computer generated number')
        return False

if (__name__ == "__main__"):
    attempts = 1
    computer_generated_no = random.randint(1,100)
    guess_number = int(input('Guess a number between 1 to 100 : '))
    result = check_number(computer_generated_no, guess_number)
    while (not result and attempts < 7):
        attempts += 1
        guess_number = int(input('Enter another number : '))
        result = check_number(computer_generated_no, guess_number)
    if (result):
        print('You won')
    elif (not result and attempts >= 7):
        print('Sorry. You fail to guess the number within 6 chances.')
