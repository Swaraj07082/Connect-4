import random

print("Welcome to Connect Four")
print("-----------------------")

possibleLetters = ["A", "B", "C", "D", "E", "F", "G"]

rows = 6
cols = 7
gameBoard = [["" for _ in range(cols)] for _ in range(rows)]

def printGameBoard():
    print("\n     A    B    C    D    E    F    G  ")
    for x in range(rows):
        print("   +----+----+----+----+----+----+----+")
        print(x, " |", end="")
        for y in range(cols):
            if gameBoard[x][y] == "🔵":
                print("", gameBoard[x][y], end=" |")
            elif gameBoard[x][y] == "🔴":
                print("", gameBoard[x][y], end=" |")
            else:
                print("    ", end="|")
        print()
    print("   +----+----+----+----+----+----+----+")

def modifyArray(spacePicked, chip):
    gameBoard[spacePicked[0]][spacePicked[1]] = chip

def checkForWinner(chip):
    for x in range(rows):
        for y in range(cols - 3):
            if all(gameBoard[x][y + i] == chip for i in range(4)):
                return True

    for x in range(rows - 3):
        for y in range(cols):
            if all(gameBoard[x + i][y] == chip for i in range(4)):
                return True

    for x in range(rows - 3):
        for y in range(cols - 3):
            if all(gameBoard[x + i][y + i] == chip for i in range(4)):
                return True

    for x in range(3, rows):
        for y in range(cols - 3):
            if all(gameBoard[x - i][y + i] == chip for i in range(4)):
                return True
    return False

def coordinateParser(inputString):
    if len(inputString) < 2 or inputString[0] not in possibleLetters:
        return None
    col = possibleLetters.index(inputString[0])
    try:
        row = int(inputString[1])
        if 0 <= row < rows:
            return [row, col]
    except ValueError:
        return None
    return None

def isSpaceAvailable(coordinate):
    row, col = coordinate
    return gameBoard[row][col] == ""

def gravityChecker(coordinate):
    row, col = coordinate
    return row == rows - 1 or gameBoard[row + 1][col] != ""

def evaluate_board():
    score = 0
    AI_WIN_SCORE = 1000
    AI_THREE_IN_A_ROW = 100
    AI_TWO_IN_A_ROW = 10
    PLAYER_THREE_IN_A_ROW = -100
    PLAYER_TWO_IN_A_ROW = -10
    CENTER_COLUMN_BONUS = 3

#     gameBoard = [
#     ["", "", "", "🔴", "", "", ""],
#     ["", "", "", "🔴", "", "", ""],
#     ["", "", "", "", "", "", ""],
#     ["", "", "", "🔵", "", "", ""],
#     ["", "", "", "", "", "", ""],
#     ["", "", "", "🔵", "", "", ""],
# ]


# center_column = ["🔴", "🔴", "", "🔵", "", "🔵"]


    center_column = [row[cols // 2] for row in gameBoard]
    center_score = center_column.count("🔴") * CENTER_COLUMN_BONUS
    score += center_score

    for x in range(rows):
        for y in range(cols - 3):
            window = [gameBoard[x][y + i] for i in range(4)]
            score += evaluate_window(window)

    for x in range(rows - 3):
        for y in range(cols):
            window = [gameBoard[x + i][y] for i in range(4)]
            score += evaluate_window(window)

    for x in range(rows - 3):
        for y in range(cols - 3):
            window = [gameBoard[x + i][y + i] for i in range(4)]
            score += evaluate_window(window)

    for x in range(3, rows):
        for y in range(cols - 3):
            window = [gameBoard[x - i][y + i] for i in range(4)]
            score += evaluate_window(window)

    return score

def evaluate_window(window):
    if window.count("🔴") == 4:
        return 1000
    elif window.count("🔴") == 3 and window.count("") == 1:
        return 100
    elif window.count("🔴") == 2 and window.count("") == 2:
        return 10
    elif window.count("🔵") == 3 and window.count("") == 1:
        return -100
    elif window.count("🔵") == 2 and window.count("") == 2:
        return -10
    return 0

def minimax(board, depth, maximizingPlayer, alpha, beta):
    #depth: The maximum depth to search in the game tree. This limits how many moves ahead we will look.

    # maximizingPlayer: A boolean flag that indicates whether the current player is the maximizing player (AI) or the minimizing player (human). This allows the algorithm to alternate between maximizing and minimizing the evaluation function.
    
    #alpha: The best score that the maximizing player can guarantee so far. If the maximizing player can get a higher score than alpha, it updates alpha.

    # beta: The best score that the minimizing player can guarantee so far. If the minimizing player can get a lower score than beta, it updates beta.
    if depth == 0 or checkForWinner("🔴") or checkForWinner("🔵"):
        return evaluate_board(), None

#         evaluate_board(): A function that evaluates the current board's state and returns a score. The score represents how favorable the current state is for the maximizing player. A positive value usually means a good state for the AI, and a negative value means a good state for the human player.
# None: The second value returned (best move) is None because there’s no specific move to recommend at this depth (it's a terminal state like a win/loss).




    valid_moves = [col for col in range(cols) if isSpaceAvailable((0, col))]

    # valid_moves = [0, 2, 6]


#     Row 0 is empty: If the top row (0) is empty, it means there is space in the column, and we can drop a piece there. Hence, isSpaceAvailable((0, col)) checks whether the top-most space is free.
# Row 0 is occupied: If row 0 is occupied, we don't want to allow a piece to be placed there, but we know there may still be room lower down (in rows 1, 2, 3, etc.), so we check the next available row.


    best_move = random.choice(valid_moves)

    if maximizingPlayer:
        max_eval = float("-inf")
        for col in valid_moves:
            row = get_next_open_row(col)
            if row is not None:
                board[row][col] = "🔴"
                eval, _ = minimax(board, depth - 1, False, alpha, beta)
                board[row][col] = ""
                if eval > max_eval:
                    max_eval = eval
                    best_move = col
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
        return max_eval, best_move

#         For each valid move: Loop through each column where a move can be made.
# row = get_next_open_row(col): Get the next available row for the current column where the piece can be dropped.
# board[row][col] = "🔴": Simulate making a move by placing the AI's token ("🔴") in the selected spot.
# eval, _ = minimax(board, depth - 1, False, alpha, beta): Recursively call minimax to evaluate the next board state. The depth - 1 decreases the depth, and False indicates that it’s the minimizing player's turn next.
# board[row][col] = "": Undo the move by resetting the board.
# if eval > max_eval:: If the evaluation of this move is better than the current best evaluation, update max_eval and set this column as the best_move.
# alpha = max(alpha, eval): Update alpha to be the maximum between the current alpha and the evaluation (eval). This keeps track of the best score the maximizing player can guarantee.
# if beta <= alpha:: If beta (the best score the minimizing player can guarantee) is less than or equal to alpha, prune the remaining branches. There's no need to search further because the minimizing player will never let the maximizing player get a score better than alpha.
# break: Stop searching further columns, as the rest are pruned.
    else:
        min_eval = float("inf")
        for col in valid_moves:
            row = get_next_open_row(col)
            if row is not None:
                board[row][col] = "🔵"
                eval, _ = minimax(board, depth - 1, True, alpha, beta)
                board[row][col] = ""
                if eval < min_eval:
                    min_eval = eval
                    best_move = col
                beta = min(beta, eval)
                if beta <= alpha:
                    break
        return min_eval, best_move

def get_next_open_row(col):
    for row in range(rows - 1, -1, -1):
#         The range(rows - 1, -1, -1) creates a sequence of row indices starting from the bottom-most row (rows - 1) to the top row (0), moving in reverse order.
# This ensures the function checks from the bottom of the column (where pieces naturally fall in Connect Four) upwards.


# row 5: 🔴
# row 4: 🔵
# row 3: 
# row 2: 
# row 1: 
# row 0: 
# Starting at row 5, it checks gameBoard[5][2], which is "🔴". Not empty, so it moves to the next row.
# At row 4, it checks gameBoard[4][2], which is "🔵". Not empty, so it moves again.
# At row 3, it checks gameBoard[3][2], which is "". The condition is True, so it returns row 3.
        if gameBoard[row][col] == "":
            return row
    return None

def playerTurn():
    while True:
        spacePicked = input("\nChoose a space (e.g., A0, B1): ").upper()
        coordinate = coordinateParser(spacePicked)
        if coordinate is None:
            print("Invalid input! Please enter a valid coordinate (e.g., A0, B1).")
            continue
        if isSpaceAvailable(coordinate) and gravityChecker(coordinate):
            modifyArray(coordinate, "🔵")
            return True
        else:
            print("Invalid move! Please pick an available column that follows gravity rules.")

def computerTurn():
    print("\nComputer is thinking...")
    _, best_move = minimax(gameBoard, depth=4, maximizingPlayer=True, alpha=float("-inf"), beta=float("inf"))
    row = get_next_open_row(best_move)
    if row is not None:
        modifyArray([row, best_move], "🔴")
        return True

def main():
    turnCounter = 0
    while True:
        printGameBoard()
        if turnCounter % 2 == 0:
            print("\nPlayer's turn")
            if playerTurn():
                if checkForWinner("🔵"):
                    printGameBoard()
                    print("\n🎉 Player wins! Thank you for playing! 🎉")
                    break
        else:
            print("\nComputer's turn")
            if computerTurn():
                if checkForWinner("🔴"):
                    printGameBoard()
                    print("\n💻 Computer wins! Better luck next time! 💻")
                    break

        turnCounter += 1

    print("\nGame over. Thank you for playing!")

# Start the game
main()
