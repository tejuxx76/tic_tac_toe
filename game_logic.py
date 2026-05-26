import random

win_positions = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8],
    [0, 3, 6], [1, 4, 7], [2, 5, 8],
    [0, 4, 8], [2, 4, 6]
]

def check_winner(board):
    for pos in win_positions:
        a, b, c = pos
        if board[a] == board[b] == board[c] != "":
            return pos
    return None

def computer_move(board):
    empty_cells = [i for i in range(9) if board[i] == ""]

    # Computer winning move
    for i in empty_cells:
        board[i] = "O"
        if check_winner(board):
            board[i] = ""
            return i
        board[i] = ""

    # Block player winning move
    for i in empty_cells:
        board[i] = "X"
        if check_winner(board):
            board[i] = ""
            return i
        board[i] = ""

    if 4 in empty_cells:
        return 4

    if empty_cells:
        return random.choice(empty_cells)

    return None