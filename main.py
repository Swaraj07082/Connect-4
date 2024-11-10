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