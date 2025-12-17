# Title And Description 🎮
This repository is a collection of simple games created using Python. Whether you're a beginner looking to learn Python or a seasoned developer seeking inspiration, explore and enjoy a wide variety of classic and original games right here.

## Table of Contents
- Introduction of Core Python 
- Usage
- Features
- Games List
- Requirements
- Code Snippets
- Author and License

### Introduction of Python
Python is a versatile programming language, and what better way to explore its capabilities than through the world of games? This repository is a labour of love, aiming to provide a wide range of games to learn from, customize, or simply enjoy. Each game is kept simple to encourage exploration and modification.

### Usage
Play the common games like rock🪨-paper📄-scissors✂️, tic-tac-toe❎0️⃣, seven-up7️⃣⬆️7️⃣⬇️, guess a number, hangman, etc. without the graphical interface very easily

### Features
- Beginner-friendly games
- Uses Python's different modules
- Runs in the command line without GUI
- Simple and easy to understand logic

### Games List
- <b>Rock Paper Scissors:</b> A game where the player chooses rock, paper, or scissors to compete against the computer.
- <b>Tic Tac Toe:</b> Create a two-player tic-tac-toe game.
- <b>Hangman:</b> A classic word-guessing game where the player tries to guess a hidden word letter by letter.
- <b>Seven Up Seven Down:</b> Guess number between 1 to 10 and find whether its begger than 7 or not.
- <b>Snake and Ladder:</b> Single player snake and ladder game where if snake eats you fall down and if you reach ladder, you move up to reach 100 fastest.
- <b>Guess a Number:</b> A game where user gets maximum 6 chances to guess a computer generated random number between 1 to 100.

### Requirements
Python version 3.13.5(base)

### Code Snippets
Some of the code snippets of few games are:

<i><b> For Rock_Paper_Scissors: </b></i> <br>

    import random
    def check():
        if (user_option == comp_option):
            print ('\nGame tie')
        elif ((user_option == 1 and comp_option==2) or (user_option == 2 and comp_option == 3) or (user_option == 3 and comp_option == 1)):
            print ('\nComputer won')
        elif ((user_option == 1 and comp_option==3) or (user_option == 2 and comp_option == 1) or (user_option == 3 and comp_option == 2)):
            print ('\nYou won')


<i><b>For Hangman:</b></i> <br>
    
    for i in range(len):
        try_word.insert(i,'*')
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

<i><b>For Tic-Tac-Toe:</b></i> <br>

        def player_move(player_symbol):
            """Gets a valid move from the current player."""
            while True:
                try:
                    move = int(input(f"Player {player_symbol}, enter your move (1-9): ")) - 1
                    if 0 <= move <= 8 and board[move] == ' ':
                        return move
                    else:
                        print("Invalid move or spot already taken. Try again.")
                except ValueError:
                    print("Invalid input. Please enter a number between 1 and 9.")


        def check_win(board, player_symbol):
            """Checks if the current player has won."""
            winning_combinations = [
                (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
                (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
                (0, 4, 8), (2, 4, 6)              # Diagonals
            ]
            for combo in winning_combinations:
                if all(board[i] == player_symbol for i in combo):
                    return True
            return False


### Author and License
<i><b>Niki Kothari</b></i>
