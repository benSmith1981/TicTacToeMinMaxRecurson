board = [
[" "," "," "],
[" "," "," "],
[" "," "," "]
]
def check_winner(board):

    # rows 
    for row in board:
        # we check if all three cells in the row are the same and not empty. 
        # If they are, we return the mark of the winner (X or O).
        if row[0] == row[1] == row[2] != " ":
            return row[0]

    # columns
    for col in range(3):
        # we check if all three cells in the column are the same and not empty. 
        # If they are, we return the mark of the winner (X or O).
        if board[0][col] == board[1][col] == board[2][col] != " ":
            return board[0][col]

    # diagonals
    # we check the two diagonals of the board. If all three cells in a diagonal are the same and not empty,
    # we return the mark of the winner (X or O).
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]

    # we check the other diagonal (top-right to bottom-left). If all three cells in this diagonal are the same and not empty,
    # we return the mark of the winner (X or O).
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]

    return None

def minimax(board, is_max):
    # check for winner because if there is a winner, we want to return a score immediately
    winner = check_winner(board)
    # if X wins, return +1, if O wins, return -1, if tie return 0
    # This is the base case for our recursive minimax function. If there is a winner, we return a score based on who won. 
    # If there is a tie, we return 0. If there is no winner and the board is not full, we continue with the minimax algorithm.
    # X = AI player, the one we want to maximize the score for. 
    if winner == "X":
        return 1
    # O = human opponent, the one we want to minimize the score for  :(
    if winner == "O":
        return -1

    # check if board full
    if all(cell != " " for row in board for cell in row):
        return 0

    # if it's the maximizing player's turn (AI), we want to maximize the score. 
    # If it's the minimizing player's turn (human), we want to minimize the score.
    # is_max is a boolean that indicates whether it's the maximizing player's turn or the minimizing player's turn.
    if is_max:
        # we initialize best_score to a very low value because we want to maximize it.
        best_score = -999

        # we loop through all cells on the board. If a cell is empty, we simulate placing the maximizing 
        # player's mark (X) in that cell, then we call minimax recursively to evaluate the score of that move. 
        # After evaluating the score, we undo the move (backtrack) and update best_score if the score of that 
        # move is greater than the current best_score.
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
                    # update best score if needed
                    best_score = max(score, best_score)

        return best_score

    else:
        # we initialize best_score to a very high value because we want to minimize it.
        best_score = 999
        # we loop through all cells on the board. If a cell is empty, we simulate placing the minimizing
        # player's mark (O) in that cell, then we call minimax recursively to evaluate the score of that move.
        for r in range(3):
            for c in range(3):
                # check if cell is empty
                if board[r][c] == " ":
                    # simulate the move
                    board[r][c] = "O"
                    # compute minimax score for this move
                    score = minimax(board, True)
                    # undo the move
                    board[r][c] = " "
                    # update best score if needed
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

def print_board(board):
    for row in board:
        print("|".join(row))
        print("-"*5)

def human_move(board):

    while True:
        r = int(input("Row (0-2): "))
        c = int(input("Col (0-2): "))

        if board[r][c] == " ":
            board[r][c] = "O"
            break
        else:
            print("Cell already taken!")

while True:

    print_board(board)

    # human turn
    human_move(board)

    winner = check_winner(board)
    if winner:
        print_board(board)
        print(winner, "wins!")
        break

    if all(cell != " " for row in board for cell in row):
        print("Draw!")
        break

    # AI turn
    r, c = best_move(board)
    board[r][c] = "X"

    print("AI plays:", r, c)

    winner = check_winner(board)
    if winner:
        print_board(board)
        print(winner, "wins!")
        break