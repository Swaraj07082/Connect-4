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
   
    for y in range(rows):
        for x in range(cols-3):
            if(gameBoard[x][y]==chip and gameBoard[x+1][y]==chip and gameBoard[x+2][y]==chip and gameBoard[x+3][y]==chip):
                print("\n Game Over",chip," Wins! Thank you for playing")
                return True

    
    for y in range(rows):
        for x in range(cols-3):
            if(gameBoard[x][y]==chip and gameBoard[x][y+1]==chip and gameBoard[x][y+2]==chip and gameBoard[x][y+3]==chip):
                print("\n Game Over",chip," Wins! Thank you for playing")
                return True

    for y in range(rows-3):
        for x in range(3,cols):
            if(gameBoard[x][y]==chip and gameBoard[x+1][y-1]==chip and gameBoard[x+2][y-2]==chip and gameBoard[x+3][y-3]==chip):
                print("\n Game Over",chip," Wins! Thank you for playing")
                return True


    for y in range(rows-3):
        for x in range(cols-3):
            if(gameBoard[x][y]==chip and gameBoard[x+1][y+1]==chip and gameBoard[x+2][y+2]==chip and gameBoard[x+3][y+3]==chip):
                print("\n Game Over",chip," Wins! Thank you for playing")
                return True

    return False

def coordinateParser(inputStr):
    coordinate=[None]*2
    if (inputStr[0]=="A"):
        coordinate[1]==0
    elif(inputStr[0]=="B"):
        coordinate[1]==1
    elif (inputStr[0] == "C"):
        coordinate[1] == 2
    elif (inputStr[0] == "D"):
        coordinate[1] == 3
    elif (inputStr[0] == "E"):
        coordinate[1] == 4
    elif (inputStr[0] == "F"):
        coordinate[1] == 5
    elif (inputStr[0] == "G"):
        coordinate[1] == 6
    else:
        print("Invalid choice")
    coordinate[0]=int(inputStr[1])
    return coordinate

def isSpaceAvailable(intended):
    if(gameBoard[intended[0]][intended[1]]=='🔴'):
        return False
    elif(gameBoard[intended[0]][intended[1]]=='🔵'):
        return False
    else:
        return True


def gravityChecker(intendedCoordinate):
  spaceBelow = [None] * 2
  spaceBelow[0] = intendedCoordinate[0] + 1
  spaceBelow[1] = intendedCoordinate[1]

  if(spaceBelow[0] == 6):
    return True
  
  if(isSpaceAvailable(spaceBelow) == False):
    return True
  return False