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
def isGameWon(turn, noughtsAndCrosses):
    # noughtsAndCrosses = dictToArray(boardDict)
    streakCount = 0
    # check rows for winning streak
    i = 0
    j = 0
    while i < 3:
        while j < 3:
            # print(noughtsAndCrosses[i][j] + " ", end="")
            if turn in noughtsAndCrosses[i][j]:
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
            if turn in noughtsAndCrosses[i][j]:
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
            if turn in noughtsAndCrosses[i][j]:
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
            if turn in noughtsAndCrosses[i][j]:
                streakCount += 1
            j -= 1
            i -= 1
        print()
    if streakCount == 3:
        print("2nd diagonal")
        return True

    return False


def mainLoop(oWinNum, xWinNum):
    turn = "X"
    gameWon = False
    theBoard = getNewBoard()
    for i in range(9):

        try:
            # clearScreen()
            # printBoard(theBoard)
            time.sleep(SLEEP_PERIOD)  # Add a 1-second pause to reduce flickering.
            # print("Turn for " + turn + ". Move on which space?")
            # move = input()
            move = getRandomMove(theBoard)
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
                    print("O won " + str(oWinNum))
                    print()
                else:
                    xWinNum += 1
                    print("X won " + str(xWinNum))
                    print()
                # print(turn + " won")
                break
            # if turn == "X":
            if "X" in turn:
                turn = "O"
            else:
                turn = "X"
        except KeyboardInterrupt:
            print("Bye")
            sys.exit()
    if not gameWon:
        print("Game Drawn")
        print()
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
    for i in range(5):
        winStats = mainLoop(oWinNum, xWinNum)
        oWinNum = winStats[0]
        xWinNum = winStats[1]
        # testGame()
    print(winStats)


gameLoop()
