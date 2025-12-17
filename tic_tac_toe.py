# Initialize the board as a list of 9 empty spaces
board = [' ' for _ in range(9)]

def print_board(board):
    """Prints the Tic-Tac-Toe board."""
    print(f"{board[0]}|{board[1]}|{board[2]}")
    print("-+-+-")
    print(f"{board[3]}|{board[4]}|{board[5]}")
    print("-+-+-")
    print(f"{board[6]}|{board[7]}|{board[8]}")

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

def check_draw(board):
    """Checks if the game is a draw."""
    return ' ' not in board

def play_game():
    """Manages the game flow."""
    current_player = 'X'
    game_over = False

    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    while not game_over:
        move = player_move(current_player)
        board[move] = current_player
        print_board(board)

        if check_win(board, current_player):
            print(f"Player {current_player} wins!")
            game_over = True
        elif check_draw(board):
            print("It's a draw!")
            game_over = True
        else:
            current_player = 'O' if current_player == 'X' else 'X'

# Start the game
if __name__ == "__main__":
    play_game()