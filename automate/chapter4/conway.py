# Conway's Game of Life
import random
import time
import copy
import os
import sys
import shutil

# from termcolor import colored, cprint

SLEEP_PERIOD = 1
HEADER = "\033[95m"
OKBLUE = "\033[94m"
OKCYAN = "\033[96m"
OKGREEN = "\033[92m"
WARNING = "\033[93m"
FAIL = "\033[91m"
ENDC = "\033[0m"
BOLD = "\033[1m"
UNDERLINE = "\033[4m"
args = None
if args is None:
    args = sys.argv[1:]

# germ = ""
germ = " # "
noGerm = "   "
currentCells = []

# Get the width and height of the terminal
rows, columns = os.popen("stty size", "r").read().split()
TERM_WIDTH = int(columns)
TERM_HEIGHT = int(rows)
WIDTH = 20
HEIGHT = 20

cellWidth = WIDTH * germ.__len__()

try:
    WIDTH = int(args[0])
    HEIGHT = int(args[1])
except IndexError:
    pass


class MyGerm:
    # isAboutToDie = False
    # germChar = ""

    def __init__(self):
        self.isAlive = True
        self.isAboutToDie = False
        self.germChar = germ
        self.noGermChar = germ


def randomCellsGenerator():
    # Create a list of list for the cells:
    randCells = []
    for x in range(WIDTH):
        column = []  # Create a new column.
        for y in range(HEIGHT):
            if random.randint(0, 1) == 0:
                myGerm = MyGerm()
                myGerm.isAlive = True
                myGerm.germChar = germ
                column.append(myGerm)  # Add a living cell.
            else:

                myGerm = MyGerm()
                myGerm.isAlive = False
                myGerm.germChar = noGerm
                column.append(myGerm)  # Add a dead cell.
        randCells.append(column)  # randCells is a list of column lists.
    return randCells


# Start process with random grid of cells
nextCells = randomCellsGenerator()


def print_centre(s):
    print(s.center(shutil.get_terminal_size().columns))


# Just a test function to see if I can print the grid in the center of the terminal
def printCellsCenter(currentCells):
    numSpacesX = TERM_WIDTH // 2 - cellWidth // 2
    numSpacesY = TERM_HEIGHT // 2 - HEIGHT // 2
    for x in range(numSpacesY):
        print()
    for y in range(HEIGHT):
        # push the grid right
        for i in range(numSpacesX):
            print(" ", end="")
        for x in range(WIDTH):
            # print(x, y, end="")
            # print(" x ", end="")
            print(currentCells[x][y].germChar, end="")  # Print the # or space.
        print()


def printCells(currentCells):
    cells = ""
    # Print currentCells on the screen:
    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(currentCells[x][y].germChar, end="")  # Print the # or space.
            # cprint(currentCells[x][y].germChar, "red", end="")  # Print the # or space.
            # cells += currentCells[x][y]
        print()  # Print a newline at the end of the row.
        # cells += "\n"
    return cells


def clearScreen():
    #     update terminal without flickering, as described at:
    #    https://stackoverflow.com/questions/69870429/how-can-i-update-clear-the-console-without-blinking-in-python
    # print("")
    termHeightPlusOne = TERM_HEIGHT
    termHeightPlusOne = str(termHeightPlusOne)
    print("\033[" + termHeightPlusOne + "A\033[2K", end="")
    # os.system("cls" if os.name == "nt" else "clear")


def printCellGenerations():
    while True:  # Main program loop.
        # print("\n\n\n\n\n")  # Separate each step with newlines.
        currentCells = copy.deepcopy(nextCells)

        # table = printCells(currentCells)
        # printCells(currentCells)
        printCellsCenter(currentCells)

        # cprint(table, "green")
        # print(table)
        # Calculate the next step's cells based on current step's cells:
        for x in range(WIDTH):
            for y in range(HEIGHT):
                # Get neighboring coordinates:
                # `% WIDTH` ensures leftCoord is always between 0 and WIDTH - 1
                leftCoord = (x - 1) % WIDTH
                rightCoord = (x + 1) % WIDTH
                aboveCoord = (y - 1) % HEIGHT
                belowCoord = (y + 1) % HEIGHT

                # Count number of living neighbors:
                numNeighbors = 0
                if currentCells[leftCoord][aboveCoord].germChar == germ:
                    numNeighbors += 1  # Top-left neighbor is alive.
                if currentCells[x][aboveCoord].germChar == germ:
                    numNeighbors += 1  # Top neighbor is alive.
                if currentCells[rightCoord][aboveCoord].germChar == germ:
                    numNeighbors += 1  # Top-right neighbor is alive.
                if currentCells[leftCoord][y].germChar == germ:
                    numNeighbors += 1  # Left neighbor is alive.
                if currentCells[rightCoord][y].germChar == germ:
                    numNeighbors += 1  # Right neighbor is alive.
                if currentCells[leftCoord][belowCoord].germChar == germ:
                    numNeighbors += 1  # Bottom-left neighbor is alive.
                if currentCells[x][belowCoord].germChar == germ:
                    numNeighbors += 1  # Bottom neighbor is alive.
                if currentCells[rightCoord][belowCoord].germChar == germ:
                    numNeighbors += 1  # Bottom-right neighbor is alive.

                # Set cell based on Conway's Game of Life rules:
                if currentCells[x][y].germChar == germ and (
                    numNeighbors == 2 or numNeighbors == 3
                ):
                    # Living cells with 2 or 3 neighbors stay alive:
                    myGerm = MyGerm()
                    myGerm.isAlive = True
                    myGerm.germChar = germ
                    myGerm.isAboutToDie = False
                    nextCells[x][y] = myGerm
                elif currentCells[x][y].germChar == " " and numNeighbors == 3:
                    # Dead cells with 3 neighbors become alive:
                    myGerm = MyGerm()
                    myGerm.isAlive = True
                    myGerm.germChar = germ
                    myGerm.isAboutToDie = False
                    nextCells[x][y] = myGerm
                else:
                    # Everything else dies or stays dead:
                    myGerm = MyGerm()
                    myGerm.isAlive = False
                    myGerm.germChar = " "
                    myGerm.isAboutToDie = False
                    nextCells[x][y] = myGerm

        time.sleep(SLEEP_PERIOD)  # Add a 1-second pause to reduce flickering.
        clearScreen()


printCellGenerations()
# print_centre("Hello World")
# printCellsCenter()
