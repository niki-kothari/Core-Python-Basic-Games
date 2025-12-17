import random

dict_ladder = {5:58, 14:49, 42:60, 53:72, 64:83, 75:94}
dict_snake = {38:20, 45:7, 51:10, 65:54, 91:73, 97:61}

p1 = 0

list_ladder = list(dict_ladder.keys())
list_snake = list(dict_snake.keys())

while (p1 < 100):
    dice = random.randint(1,6)
    print (f'Dice value is {dice}')

    if (p1 == 0 and dice==1):
        p1 = 1
        print ('Let\'s start the game')
    else:
        p1 += dice
        print ('After roll, you are on position : ', p1)
        for i in list_ladder:
            if (i == p1):
                print (f'You found ladder.\n\tBefore you was on {p1}')
                p1 = dict_ladder[i]
                print (f'\tNow you are on {p1}')
            
        for i in list_snake:
            if (i == p1):
                print (f'Snake bite you.\n\tBefore you was on {p1}')
                p1 = dict_snake[i]
                print (f'\tNow you are on {p1}')

print ("Hurray! You reached 100.")
