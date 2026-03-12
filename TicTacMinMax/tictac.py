board = [
[" "," "," "],
[" "," "," "],
[" "," "," "]
]
def check_winner(board):

    # rows
    for row in board:
        if row[0] == row[1] == row[2] != " ":
            return row[0]

    # columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != " ":
            return board[0][col]

    # diagonals
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]

    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]

    return None

def minimax(board, is_max):
    # check for winner because if there is a winner, we want to return a score immediately
    winner = check_winner(board)
    # if X wins, return +1, if O wins, return -1, if tie return 0
    # This is the base case for our recursive minimax function. If there is a winner, we return a score based on who won. 
    # If there is a tie, we return 0. If there is no winner and the board is not full, we continue with the minimax algorithm.
# X = AI player
# O = human opponent
    if winner == "X":
        return 1
    if winner == "O":
        return -1

    # check if board full
    if all(cell != " " for row in board for cell in row):
        return 0

    if is_max:
        best_score = -999

        for r in range(3):
            for c in range(3):
                if board[r][c] == " ":
                    board[r][c] = "X"

                    score = minimax(board, False)

                    board[r][c] = " "

                    best_score = max(score, best_score)

        return best_score

    else:
        best_score = 999

        for r in range(3):
            for c in range(3):
                if board[r][c] == " ":
                    board[r][c] = "O"

                    score = minimax(board, True)

                    board[r][c] = " "

                    best_score = min(score, best_score)

        return best_score

def best_move(board):

    best_score = -999
    move = None
    # loop through all cells, evaluate minimax score for each empty cell, and return the move with the highest score
    for r in range(3):
        for c in range(3):
            # check if cell is empty
            if board[r][c] == " ":
                # simulate the move
                board[r][c] = "X"
                # compute minimax score for this move
                score = minimax(board, False)
                # undo the move
                board[r][c] = " "
                # update best score and move if needed
                if score > best_score:
                    # update best score
                    best_score = score
                    # store the best move
                    move = (r,c)

    return move

move = best_move(board)