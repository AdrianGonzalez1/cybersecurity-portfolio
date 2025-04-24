import random

def display_board(board):
    print()
    print(f" {board[0]} | {board[1]} | {board[2]}")
    print("---|---|---")
    print(f" {board[3]} | {board[4]} | {board[5]}")
    print("---|---|---")
    print(f" {board[6]} | {board[7]} | {board[8]}")
    print()

def check_win(board, player):
    wins = [
        (0,1,2), (3,4,5), (6,7,8),  # rows
        (0,3,6), (1,4,7), (2,5,8),  # columns
        (0,4,8), (2,4,6)            # diagonals
    ]
    for a, b, c in wins:
        if board[a] == board[b] == board[c] == player:
            return True
    return False

def board_full(board):
    return all(space in ['X', 'O'] for space in board)

def player_move(board):
    while True:
        try:
            move = int(input("Enter your move (1-9): "))
            if move < 1 or move > 9:
                print("Invalid input. Please enter a number between 1 and 9.")
            elif board[move - 1] in ['X', 'O']:
                print("That square is already taken. Try again.")
            else:
                board[move - 1] = 'O'
                break
        except ValueError:
            print("Invalid input. Please enter a number.")

def computer_move(board):
    free_spaces = [i for i in range(9) if board[i] not in ['X', 'O']]
    if free_spaces:
        move = random.choice(free_spaces)
        board[move] = 'X'
        print(f"Computer chose position {move + 1}")

def main():
    board = [str(i+1) for i in range(9)]

    # Computer's first move
    board[4] = 'X'
    print("Welcome to Tic-Tac-Toe!")
    display_board(board)

    while True:
        # Player move
        player_move(board)
        display_board(board)
        if check_win(board, 'O'):
            print("Congratulations, you win!")
            break
        if board_full(board):
            print("It's a tie!")
            break

        # Computer move
        computer_move(board)
        display_board(board)
        if check_win(board, 'X'):
            print("Computer wins! Better luck next time.")
            break
        if board_full(board):
            print("It's a tie!")
            break

if __name__ == "__main__":
    main()
