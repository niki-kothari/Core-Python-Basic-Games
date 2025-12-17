if (__name__ == "__main__"):
    guess_word = input ('Enter your word to guess : ')
    len = len(guess_word)
    try_word = []
    win_status = False
    for i in range(len):
        try_word.insert(i,'_')
    print (try_word)
    for i in range(6):
        print (f'This is your {i+1} turn')
        char = input('Enter a character : ')
        if (guess_word == char):
            print ('\nCongratulations! YOU WON.')
            win_status = True 
            break

        counter = 0
        for j in guess_word:
            if (j == char):
                try_word[counter] = char
            counter += 1
        print (f'After {i+1} turn, you guessed ', try_word)

    if (not win_status):
        seperator = ""
        final_word = seperator.join(try_word)
        if (guess_word == final_word):
            print ('\nCongratulations! YOU WON.')
        else:
            print ('\nSorry! Better luck next time.')
            print (f'\tYour word to guess was {guess_word}')
