import os
import sys
import random
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
    # print("")
    termHeightPlusOne = TERM_HEIGHT
    termHeightPlusOne = str(termHeightPlusOne)
    print("\033[" + termHeightPlusOne + "A\033[2K", end="")
    # os.system("cls" if os.name == "nt" else "clear")


def printBoard(board):
    center_x_string = getCenterStringX2()
    # print(getCenterStringY2())
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


def getRandomMove():
    emptyList = []
    for k in theBoard.keys():
        # print(k + " ", end="")
        if theBoard[k] == " ":
            emptyList.append(k)
    # print("possible moves are ")
    # print(emptyList)
    # print("random move is")
    # print(random.choice(emptyList))
    return random.choice(emptyList)


# Each time a player makes a move, check if they have won.
# For each position, check the cells in the column and row.
# For corners, or the center, check the diagonal.
def isGameWon(turn, move):
    print("turn is" + turn)
    print("move is " + move)
    if "top" in move:
        print("Your in the top row")
    elif "mid" in move:
        print("Your in the top row")
    elif "low" in move:
        print("Your in the top row")
    if "L" in move:
        print("Your in the Left column")
    if "M" in move:
        print("Your in the Left column")
    if "R" in move:
        print("Your in the Left column")
    emptyList = []
    twoDArray = []
    for k in theBoard.keys():
        print(k, end="")

    # print(theBoard[k])


def mainLoop():
    turn = "X"
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
            isGameWon(turn, move)
            if turn == "X":
                turn = "O"
            else:
                turn = "X"
            printBoard(theBoard)
        except KeyboardInterrupt:
            print("Bye")
            sys.exit()


mainLoop()
