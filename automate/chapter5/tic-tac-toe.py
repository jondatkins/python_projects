import os
import random
from re import M
import sys
import time

rows, columns = os.popen("stty size", "r").read().split()
TERM_WIDTH = int(columns)
TERM_HEIGHT = int(rows)
# The widht and height of the grid in cells
WIDTH = 10
HEIGHT = 10
SLEEP_PERIOD = 0.5
NUM_GAME_LOOPS = 6
PLAYERS = ("X", "Y")
GRID_WIDTH = 3


def getNewBoard():
    theBoard = {
        "top-L": " ",
        "top-M": " ",
        "top-R": " ",
        "mid-L": " ",
        "mid-M": " ",
        "mid-R": " ",
        "low-L": " ",
        "low-M": " ",
        "low-R": " ",
    }
    return theBoard


def getNewBoard2():
    # board = []
    # Creates a list containing 5 lists, each of 8 items, all set to 0
    w, h = GRID_WIDTH, GRID_WIDTH
    Matrix = [[" " for x in range(w)] for y in range(h)]
    # i = 0
    # j = 0
    # while i < 3:
    #     while j < 3:
    #         Matrix[i][j] = " "
    #     j = 0
    #     i += 1
    return Matrix


player1 = "X"
player2 = "O"
cellWidth = WIDTH * len(player1)
# print("cellwidth is " + str(cellWidth))

colourDict = {
    "HEADER": "\033[95m",
    "OKBLUE": "\033[94m",
    "OKCYAN": "\033[96m",
    "OKGREEN": "\033[92m",
    "WARNING": "\033[93m",
    "FAIL": "\033[91m",
    "ENDC": "\033[0m",
    "BOLD": "\033[1m",
}

colourList = list(colourDict.values())


# gets a random colour for each cell in the grid.
def getColouredCharacter(char):
    colour = random.choice(colourList)
    colourEnd = colourDict["ENDC"]
    colourChar = colour + char + colourEnd
    return colourChar


def getCenterStringX2():
    # push the grid right
    widthSpacerString = ""
    numSpacesX = (TERM_WIDTH // 2) - (cellWidth // 2)
    for i in range(numSpacesX):
        # print(" ", end="")
        widthSpacerString += " "
    return widthSpacerString


def getCenterStringY2():
    numSpacesY = TERM_HEIGHT // 2 - HEIGHT // 2
    carrReturn = ""
    for x in range(numSpacesY):
        carrReturn += "\n"
    return carrReturn


def clearScreen():
    #     update terminal without flickering, as described at:
    #    https://stackoverflow.com/questions/69870429/how-can-i-update-clear-the-console-without-blinking-in-python
    termHeightPlusOne = TERM_HEIGHT
    termHeightPlusOne = str(termHeightPlusOne)
    print("\033[" + termHeightPlusOne + "A\033[2K", end="")
    # os.system("cls" if os.name == "nt" else "clear")


def getRandomMove(theBoard):
    emptyList = []
    for k in theBoard.keys():
        if theBoard[k] == " ":
            emptyList.append(k)
    return random.choice(emptyList)


def getRandomMove2(theBoard):
    i = 0
    j = 0
    k = 0
    arrayCopy = []
    while i < GRID_WIDTH:
        while j < GRID_WIDTH:
            if theBoard[i][j] == " ":
                matrixCoord = (i, j)
                arrayCopy.append(matrixCoord)
                k += 1
            j += 1
        j = 0
        i += 1
    # print(arrayCopy)
    randIndex = random.randint(0, len(arrayCopy) - 1)
    # print(randIndex)
    return arrayCopy[randIndex]


def printBoard(board):
    center_x_string = getCenterStringX2()
    print(getCenterStringY2())
    print(
        center_x_string + board["top-L"] + "|" + board["top-M"] + "|" + board["top-R"]
    )
    print(center_x_string + "-+-+-")
    print(
        center_x_string + board["mid-L"] + "|" + board["mid-M"] + "|" + board["mid-R"]
    )
    print(center_x_string + "-+-+-")
    print(
        center_x_string + board["low-L"] + "|" + board["low-M"] + "|" + board["low-R"]
    )


def printBoard2(board):
    center_x_string = getCenterStringX2()
    print(getCenterStringY2())
    i = 0
    j = 0
    while i < GRID_WIDTH:
        print(center_x_string, end="")
        while j < GRID_WIDTH:
            if j == GRID_WIDTH - 1:
                print(board[i][j], end="")
            else:
                print(board[i][j] + "|", end="")
            j += 1
        # print(center_x_string, end="")
        print()

        if i != GRID_WIDTH - 1:
            print(center_x_string + "-+-+-")
        # print("\n-+-+-")
        j = 0
        i += 1


def print2dArray(twoDArray):
    i = 0
    j = 0
    while i < 3:
        while j < 3:
            print(twoDArray[i][j] + " ", end="")
            j += 1
        print()
        j = 0
        i += 1


def dictToArray(dict):
    noughtsAndCrosses = [
        [dict["top-L"], dict["top-M"], dict["top-R"]],
        [dict["mid-L"], dict["mid-M"], dict["mid-R"]],
        [dict["low-L"], dict["low-M"], dict["low-R"]],
    ]
    return noughtsAndCrosses


# Each time a player makes a move, check if they have won.
# check rows, columns and diagonals, return true if there's a
# winning streak of 3
def isGameWon(turn, noughtsAndCrosses):
    streakCount = 0
    # check rows for winning streak
    i = 0
    j = 0
    while i < GRID_WIDTH:
        while j < GRID_WIDTH:
            if turn in noughtsAndCrosses[i][j]:
                streakCount += 1
            j += 1
            if streakCount == GRID_WIDTH:
                return True
        streakCount = 0
        print()
        j = 0
        i += 1

    # check columns for a win
    streakCount = 0
    i = 0
    j = 0

    while j < GRID_WIDTH:
        while i < GRID_WIDTH:
            if turn in noughtsAndCrosses[i][j]:
                streakCount += 1
            i += 1
            if streakCount == GRID_WIDTH:
                return True
        j += 1
        i = 0
        streakCount = 0
        print()

    if streakCount == GRID_WIDTH:
        return True

    # check left top to bottom right diagonal
    streakCount = 0
    i = 0
    j = 0
    while i < GRID_WIDTH:
        while j < GRID_WIDTH:
            if turn in noughtsAndCrosses[i][j]:
                streakCount += 1
            j += 1
            i += 1
        print()

    if streakCount == GRID_WIDTH:
        return True

    # check top right to bottom left diagonal
    streakCount = 0
    i = 2
    j = 2
    while i >= 0:
        while j >= 0:
            if turn in noughtsAndCrosses[i][j]:
                streakCount += 1
            j -= 1
            i -= 1
        print()
    if streakCount == GRID_WIDTH:
        return True

    return False


def mainLoop(oWinNum, xWinNum):
    turn = random.choice(PLAYERS)
    gameWon = False
    theBoard = getNewBoard()
    # theBoard2 = getNewBoard2()
    for i in range(9):

        try:
            time.sleep(SLEEP_PERIOD)  # Add a 1-second pause to reduce flickering.
            # print("Turn for " + turn + ". Move on which space?")
            # move = input()
            move = getRandomMove(theBoard)
            # move2 = getRandomMove2(theBoard)
            move = str(move)

            colouredTurn = getColouredCharacter(turn)
            theBoard[move] = colouredTurn
            clearScreen()
            printBoard(theBoard)
            noughtsAndCrosses = dictToArray(theBoard)
            gameWon = isGameWon(turn, noughtsAndCrosses)
            if gameWon:
                if turn == "O":
                    oWinNum += 1
                else:
                    xWinNum += 1
                break
            if "X" in turn:
                turn = "O"
            else:
                turn = "X"
        except KeyboardInterrupt:
            print("Bye")
            sys.exit()
    # if not gameWon:
    #     print("Game Drawn")
    return [oWinNum, xWinNum]


def mainLoop2(oWinNum, xWinNum):
    turn = random.choice(PLAYERS)
    gameWon = False
    # theBoard = getNewBoard()
    theBoard = getNewBoard2()
    for i in range(GRID_WIDTH * GRID_WIDTH):

        try:
            time.sleep(SLEEP_PERIOD)  # Add a 1-second pause to reduce flickering.
            # print("Turn for " + turn + ". Move on which space?")
            # move = input()
            move = getRandomMove2(theBoard)

            colouredTurn = getColouredCharacter(turn)
            # theBoard[move] = colouredTurn
            theBoard[move[0]][move[1]] = colouredTurn
            clearScreen()
            printBoard2(theBoard)
            # noughtsAndCrosses = dictToArray(theBoard)
            gameWon = isGameWon(turn, theBoard)
            if gameWon:
                if turn == "O":
                    oWinNum += 1
                else:
                    xWinNum += 1
                break
            if "X" in turn:
                turn = "O"
            else:
                turn = "X"
        except KeyboardInterrupt:
            print("Bye")
            sys.exit()
    # if not gameWon:
    #     print("Game Drawn")
    return [oWinNum, xWinNum]


def testGame():
    gameWon = False
    turn = "O"
    turn1 = getColouredCharacter("O")
    turn2 = getColouredCharacter("O")
    turn3 = getColouredCharacter("O")
    testBoard = {
        "top-L": turn1,
        "top-M": turn2,
        "top-R": turn3,
        "mid-L": "X",
        "mid-M": "X",
        "mid-R": " ",
        "low-L": " ",
        "low-M": " ",
        "low-R": "O",
    }
    twoDArray = dictToArray(testBoard)
    print2dArray(twoDArray)

    printBoard(testBoard)
    gameWon = isGameWon(turn, twoDArray)
    print("game won " + str(gameWon))


def gameLoop():
    oWinNum = 0
    xWinNum = 0
    winStats = []
    for i in range(NUM_GAME_LOOPS):
        winStats = mainLoop2(oWinNum, xWinNum)
        oWinNum = winStats[0]
        xWinNum = winStats[1]
        # testGame()
    oWins = winStats[0]
    xWins = winStats[1]
    print("O won " + str(oWins) + " times")
    print("X won " + str(xWins) + " times")


gameLoop()
