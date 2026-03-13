import random

#board setup
board = [' ' for _ in range(9)]
def print_board():
    print()
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")
    print()
def check_winner(player):
    win_conditions = [
        [0,1,2], [3,4,5], [6,7,8],  # rows
        [0,3,6], [1,4,7], [2,5,8],  # columns
        [0,4,8], [2,4,6]            # diagonals
    ]
    for condition in win_conditions:
        if all(board[i] == player for i in condition):
            return True
    return False
def check_draw():
    return ' ' not in board
def player_move():
    while True:
        move = input("enter your move (1-9): ")
        if move.isdigit() and int(move) in range(1,10):
            move = int(move) - 1
            if board[move] == ' ':
                board[move] = 'X'
                break
            else:
                print("spot already taken!")
        else:
            print("invalid input, choose 1-9.")

def ai_move():
    #check if AI can win in next move
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            if check_winner('O'):
                return
            board[i] = ' '
    
    #block player from winning
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'X'
            if check_winner('X'):
                board[i] = 'O'
                return
            board[i] = ' '
    
    #take center if free
    if board[4] == ' ':
        board[4] = 'O'
        return
    
    #take a random corner
    corners = [i for i in [0,2,6,8] if board[i] == ' ']
    if corners:
        board[random.choice(corners)] = 'O'
        return
    
    #take any empty space
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            return

#main Game Loop
def main():
    print("=== Tic Tac Toe ===")
    print("You are X, AI is O")
    print_board()
    
    while True:
        player_move()
        print_board()
        if check_winner('X'):
            print("Congratulations! You win!")
            break
        if check_draw():
            print("It's a draw!")
            break
        
        ai_move()
        print("AI moved:")
        print_board()
        if check_winner('O'):
            print("AI wins! Better luck next time.")
            break
        if check_draw():
            print("It's a draw!")
            break

if __name__ == "__main__":
    main()