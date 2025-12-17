import random

def check():
    if (user_option == comp_option):
        print ('\nGame tie')
    elif ((user_option == 1 and comp_option==2) or (user_option == 2 and comp_option == 3) or (user_option == 3 and comp_option == 1)):
        print ('\nComputer won')
    elif ((user_option == 1 and comp_option==3) or (user_option == 2 and comp_option == 1) or (user_option == 3 and comp_option == 2)):
        print ('\nYou won')

#main
if (__name__ == '__main__'):
    print ('LETS PLAY  ROCK PAPER SCISSORS ')
    user_option = 1
    while (user_option != 0):
        print ('\nSelect your choice : ')
        print ('\t1 for Rock')
        print ('\t2 for Paper')
        print ('\t3 for Scissors')
        print ('\t0 to exit game')
        user_option = int (input ('\tEnter your choice : '))
        if (user_option == 1):
            print ('\nYou selected ROCK')
        elif (user_option == 2):
            print ('\nYou selected PAPER')
        elif (user_option == 3):
            print ('\nYou selected SCISSORS')
        elif (user_option == 0):
            print ('\nThank you.')
            break
        else:
            print ('\nWrong choice. Please select correct option.\n')
            continue

        comp_option = random.randint(1,3)
        if (comp_option == 1):
            print ('Computer selected ROCK')
        elif (comp_option == 2):
            print ('Computer selected PAPER')
        elif (comp_option == 3):
            print ('Computer selected SCISSORS')

        check()
