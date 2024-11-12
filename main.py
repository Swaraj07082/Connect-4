import random

print("Welcome to Connect Four")
print("-----------------------")

possibleLetters = ["A", "B", "C", "D", "E", "F", "G"]
gameBoard = [["" for _ in range(7)] for _ in range(6)]

rows = 6
cols = 7

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

def modifyArray(spacePicked, turn):
    gameBoard[spacePicked[0]][spacePicked[1]] = turn

def checkForWinner(chip):
    # Check horizontal spaces
    for x in range(rows):
        for y in range(cols - 3):
            if gameBoard[x][y] == chip and gameBoard[x][y+1] == chip and gameBoard[x][y+2] == chip and gameBoard[x][y+3] == chip:
                return True

    # Check vertical spaces
    for x in range(rows - 3):
        for y in range(cols):
            if gameBoard[x][y] == chip and gameBoard[x+1][y] == chip and gameBoard[x+2][y] == chip and gameBoard[x+3][y] == chip:
                return True

    # Check diagonals (bottom-left to top-right)
    for x in range(rows - 3):
        for y in range(cols - 3):
            if gameBoard[x][y] == chip and gameBoard[x+1][y+1] == chip and gameBoard[x+2][y+2] == chip and gameBoard[x+3][y+3] == chip:
                return True

    # Check diagonals (top-left to bottom-right)
    for x in range(3, rows):
        for y in range(cols - 3):
            if gameBoard[x][y] == chip and gameBoard[x-1][y+1] == chip and gameBoard[x-2][y+2] == chip and gameBoard[x-3][y+3] == chip:
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
    # Check if it's the bottom row or if there's a chip below
    return row == rows - 1 or gameBoard[row + 1][col] != ""

def playerTurn():
    while True:
        spacePicked = input("\nChoose a space (e.g., A0, B1): ").upper()
        coordinate = coordinateParser(spacePicked)
        if coordinate is None:
            print("Invalid input! Please enter a valid coordinate (e.g., A0, B1).")
            continue
        if isSpaceAvailable(coordinate) and gravityChecker(coordinate):
            modifyArray(coordinate, '🔵')
            return True
        else:
            print("Invalid move! Please pick an available column that follows gravity rules.")

def computerTurn():
    while True:
        random_col = random.choice(possibleLetters)
        random_row = random.randint(0, 5)
        coordinate = coordinateParser(random_col + str(random_row))
        if coordinate and isSpaceAvailable(coordinate) and gravityChecker(coordinate):
            modifyArray(coordinate, '🔴')
            return True

def main():
    turnCounter = 0
    while True:
        printGameBoard()
        if turnCounter % 2 == 0:
            print("\nPlayer's turn")
            if playerTurn():
                if checkForWinner('🔵'):
                    printGameBoard()
                    print("\n🎉 Player wins! Thank you for playing! 🎉")
                    break
        else:
            print("\nComputer's turn")
            computerTurn()
            if checkForWinner('🔴'):
                printGameBoard()
                print("\n💻 Computer wins! Better luck next time! 💻")
                break

        turnCounter += 1

    print("\nGame over. Thank you for playing!")

# Start the game
main()
