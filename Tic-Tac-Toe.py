import random


def drawBoard(bord):
    print("   |   |")
    print(" " + bord[0] + " | " + bord[1] + " | " + bord[2])
    print("   |   |")
    print("-----------")
    print("   |   |")
    print(" " + bord[3] + " | " + bord[4] + " | " + bord[5])
    print("   |   |")
    print("-----------")
    print("   |   |")
    print(" " + bord[6] + " | " + bord[7] + " | " + bord[8])
    print("   |   |")
    print("")
    print("x-o-x-o-x-o-x-o")
    print("")


def getBoardCopy(board):
    dupeBoard = []
    for i in board:
        dupeBoard.append(i)
    return dupeBoard


def isSpaceFree(board, move):
    return board[move] == ' '


def chooseRandomMoveFromList(board, movesList):
    possibleMoves = []
    for i in range(len(movesList)):
        if board[i] == ' ':
            possibleMoves.append(i)

    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None


def makeMove(board, letter, move):
    board[move] = letter


def owinner(bord):
    if bord[0] == bord[1] == bord[2] == o:
        return True
    elif bord[3] == bord[4] == bord[5] == o:
        return True
    elif bord[6] == bord[7] == bord[8] == o:
        return True


    elif bord[0] == bord[3] == bord[6] == o:
        return True
    elif bord[1] == bord[4] == bord[7] == o:
        return True
    elif bord[2] == bord[5] == bord[8] == o:
        return True


    elif bord[0] == bord[4] == bord[8] == o:
        return True
    elif bord[2] == bord[4] == bord[6] == o:
        return True
    else:
        return False

def xwinner(bord):
    if bord[0] == bord[1] == bord[2] == x:
        return True
    elif bord[3] == bord[4] == bord[5] == x:
        return True
    elif bord[6] == bord[7] == bord[8] == x:
        return True


    elif bord[0] == bord[3] == bord[6] == x:
        return True
    elif bord[1] == bord[4] == bord[7] == x:
        return True
    elif bord[2] == bord[5] == bord[8] == x:
        return True


    elif bord[0] == bord[4] == bord[8] == x:
        return True
    elif bord[2] == bord[4] == bord[6] == x:
        return True
    else:
        return False


def getComputerMove(board, computerLetter):
    # Given a board and the computer's letter, determine where to move and return that move.
    if computerLetter == x:
        playerLetter = o
    else:
        playerLetter = x

    # Here is our algorithm for our Tic Tac Toe AI:
    # First, check if we can win in the next move
    for i in range(0,9):
        copy = getBoardCopy(board)
        if board[i] == ' ':
            makeMove(copy, computerLetter, i)
            if xwinner(copy) == True:
                return i

    # Check if the player could win on his next move, and block them.
    for i in range(0,9):
        copy = getBoardCopy(board)
        if board[i] == ' ':
            makeMove(copy, playerLetter, i)
            if xwinner(copy) == True:
                return i

    # Try to take one of the corners, if they are free.
    move = chooseRandomMoveFromList(board, [1, 3, 7, 9])
    if move != None:
        return move

    # Try to take the center, if it is free.
    if isSpaceFree(board, 5):
        return 5

    # Move on one of the sides.
    return chooseRandomMoveFromList(board, [2, 4, 6, 8])

empty = ' '
x = "X"
o = "O"
cornerindex = [0, 2, 6, 8]
board = [empty, empty, empty, empty, empty, empty, empty, empty, empty]
won = 0
r = cornerindex[random.randint(0, 3)]
board[r] = x
drawBoard(board)
count = 0


while won == 0:
    umove = int(input("your move: "))

    board[umove-1] = o
    drawBoard(board)
    if owinner(board) == True:
        print("you have won. congratulations.")
        won = 1
        quit()

    board[getComputerMove(board, x)] = x
    if xwinner(board) == True:
        print("computer has won.")
        won = 1
        quit()
    drawBoard(board)

    for i in range(len(board)):
        if board[i] == x or o:
            count += 1
    if count == 0:
        print("game is tied")
        quit()
