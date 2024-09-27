import os
import random
import sys
import time

rows, columns = os.popen("stty size", "r").read().split()
TERM_WIDTH = int(columns)
TERM_HEIGHT = int(rows)
# The widht and height of the grid in cells
WIDTH = 10
HEIGHT = 10
SLEEP_PERIOD = 1

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
player1 = "X"
player2 = "O"
cellWidth = WIDTH * len(player1)
# print("cellwidth is " + str(cellWidth))


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


def getRandomMove():
    emptyList = []
    for k in theBoard.keys():
        if theBoard[k] == " ":
            emptyList.append(k)
    return random.choice(emptyList)


def printBoard(board):
    clearScreen()
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
    # clearScreen()


def print2dArray(twoDArray):
    i = 0
    j = 0
    while i < 3:
        while j < 3:
            print(twoDArray[i][j] + " ", end="")
            j += 1
        streakCount = 0
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
# For each position, check the cells in the column and row.
# For corners, or the center, check the diagonal.
def isGameWon(turn, boardDict):
    noughtsAndCrosses = dictToArray(boardDict)
    streakCount = 0
    # check rows for winning streak
    i = 0
    j = 0
    while i < 3:
        while j < 3:
            # print(noughtsAndCrosses[i][j] + " ", end="")
            if turn == noughtsAndCrosses[i][j]:
                streakCount += 1
            j += 1
            if streakCount == 3:
                print("row of 3")
                return True
        streakCount = 0
        print()
        j = 0
        i += 1

    # check columns for a win
    streakCount = 0
    i = 0
    j = 0

    while j < 3:
        while i < 3:
            # print(noughtsAndCrosses[i][j] + " ")
            if turn == noughtsAndCrosses[i][j]:
                streakCount += 1
            i += 1
            if streakCount == 3:
                print("column of 3")
                return True
        j += 1
        i = 0
        streakCount = 0
        print()

    if streakCount == 3:
        return True

    # check left top to bottom right diagonal
    streakCount = 0
    i = 0
    j = 0
    while i < 3:
        while j < 3:
            # print(noughtsAndCrossesTest[i][j] + " ")
            if turn == noughtsAndCrosses[i][j]:
                streakCount += 1
            j += 1
            i += 1
        print()

    if streakCount == 3:
        print("1st diagonal")
        return True

    # check top right to bottom left diagonal
    streakCount = 0
    i = 2
    j = 2
    while i >= 0:
        while j >= 0:
            if turn == noughtsAndCrosses[i][j]:
                streakCount += 1
            j -= 1
            i -= 1
        print()
    if streakCount == 3:
        print("2nd diagonal")
        return True

    return False


def mainLoop():
    turn = "X"
    gameWon = False
    for i in range(9):

        try:
            # clearScreen()
            # printBoard(theBoard)
            time.sleep(SLEEP_PERIOD)  # Add a 1-second pause to reduce flickering.
            # print("Turn for " + turn + ". Move on which space?")
            # move = input()
            move = getRandomMove()
            move = str(move)
            theBoard[move] = turn
            printBoard(theBoard)
            gameWon = isGameWon(turn, theBoard)
            if gameWon:
                print(turn + " won")
                break
            if turn == "X":
                turn = "O"
            else:
                turn = "X"
        except KeyboardInterrupt:
            print("Bye")
            sys.exit()
    if not gameWon:
        print("Game Drawn")


def testGame():
    gameWon = False
    turn = "O"
    testBoard = {
        "top-L": " ",
        "top-M": " ",
        "top-R": "O",
        "mid-L": "X",
        "mid-M": "X",
        "mid-R": "O",
        "low-L": " ",
        "low-M": " ",
        "low-R": "O",
    }
    twoDArray = dictToArray(testBoard)
    print2dArray(twoDArray)

    printBoard(testBoard)
    gameWon = isGameWon(turn, testBoard)
    print("game won " + str(gameWon))


mainLoop()
# testGame()
