print("\n          Welcome to Connect 4")
print(" -----------------------------------------")


rows = 6
cols = 7

gameBoard  = [["","","","","","","",],["","","","","","","",],["","","","","","","",],["","","","","","","",],["","","","","","","",],["","","","","","","",]]
def printGameBoard():
    print("\n     A    B    C    D    E    F    G  " , end="")
    
    for i in range(rows):
      print("\n   +----+----+----+----+----+----+----+")
      print(i, " |",end="")

      for j in range(cols):
        if(gameBoard[i][j] == "🟡"):
            print("",gameBoard[i][j],end="   |")
        elif(gameBoard[i][j] == "🔴"):
            print("",gameBoard[i][j],end="   |")
        else:
            print("",gameBoard[i][j],end="   |")

    print("\n   +----+----+----+----+----+----+----+")
printGameBoard()

def modifyTurn(spacePicked,turn):
    gameBoard[spacePicked[0]][spacePicked[1]]=turn

def checkForWinner(chip):
    # For Horizontal spaces
    for y in range(rows):
        for x in range(cols-3):
            if(gameBoard[x][y]==chip and gameBoard[x+1][y]==chip and gameBoard[x+2][y]==chip and gameBoard[x+3][y]==chip):
                print("\n Game Over",chip," Wins! Thank you for playing")
                return True

    # For vertical spaces
    for y in range(rows):
        for x in range(cols-3):
            if(gameBoard[x][y]==chip and gameBoard[x][y+1]==chip and gameBoard[x][y+2]==chip and gameBoard[x][y+3]==chip):
                print("\n Game Over",chip," Wins! Thank you for playing")
                return True

    # For diagonal spaces (Top right to Bottom right)
    for y in range(rows-3):
        for x in range(3,cols):
            if(gameBoard[x][y]==chip and gameBoard[x+1][y-1]==chip and gameBoard[x+2][y-2]==chip and gameBoard[x+3][y-3]==chip):
                print("\n Game Over",chip," Wins! Thank you for playing")
                return True

    # For diagonal spaces(Top left to bottom right) spaces
    for y in range(rows-3):
        for x in range(cols-3):
            if(gameBoard[x][y]==chip and gameBoard[x+1][y+1]==chip and gameBoard[x+2][y+2]==chip and gameBoard[x+3][y+3]==chip):
                print("\n Game Over",chip," Wins! Thank you for playing")
                return True

    return False




