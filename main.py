import math

# Board setup
board = [" " for _ in range(9)]

def print_board():
    for i in range(3):
        print(board[i*3:(i+1)*3])

def check_winner(b, player):
    win_conditions = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]
    return any(all(b[i] == player for i in cond) for cond in win_conditions)

def is_full(b):
    return " " not in b

# Minimax algorithm
def minimax(b, depth, is_maximizing):
    if check_winner(b, "O"):
        return 1
    if check_winner(b, "X"):
        return -1
    if is_full(b):
        return 0

    if is_maximizing:
        best = -math.inf
        for i in range(9):
            if b[i] == " ":
                b[i] = "O"
                score = minimax(b, depth+1, False)
                b[i] = " "
                best = max(score, best)
        return best
    else:
        best = math.inf
        for i in range(9):
            if b[i] == " ":
                b[i] = "X"
                score = minimax(b, depth+1, True)
                b[i] = " "
                best = min(score, best)
        return best

# AI move
def ai_move():
    best_score = -math.inf
    move = -1

    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(board, 0, False)
            board[i] = " "
            if score > best_score:
                best_score = score
                move = i

    board[move] = "O"

# Game loop
def play():
    print("Positions are 0 to 8")
    print_board()

    while True:
        # Human move
        move = int(input("Enter your move (0-8): "))
        if board[move] != " ":
            print("Invalid move!")
            continue

        board[move] = "X"
        print_board()

        if check_winner(board, "X"):
            print("You win!")
            break
        if is_full(board):
            print("Draw!")
            break

        # AI move
        ai_move()
        print("AI move:")
        print_board()

        if check_winner(board, "O"):
            print("AI wins!")
            break
        if is_full(board):
            print("Draw!")
            break

play()