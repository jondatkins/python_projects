# Conway's Game of Life
import random
import time
import copy
import os
import sys
import shutil


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
# The widht and height of the grid in cells
WIDTH = 20
HEIGHT = 20


try:
    WIDTH = int(args[0])
    HEIGHT = int(args[1])
    if WIDTH > TERM_WIDTH:
        WIDTH = TERM_WIDTH
    if HEIGHT > TERM_HEIGHT:
        HEIGHT = TERM_HEIGHT
except IndexError:
    pass

# The width of the grid is WIDTH * the length of the germ character
cellWidth = WIDTH * germ.__len__()


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


class bcolors:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKCYAN = "\033[96m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"


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

# my_dict = {"Dave": "001", "Ava": "002", "Joe": "003"}
# print(my_dict.keys())
# print(my_dict.values())
# print(my_dict.get("Dave"))


colourList = list(colourDict.values())
# colourList.remove("\033[0m")


# Just a test function to see if I can print the grid in the center of the terminal
def printCellsCenter(currentCells):
    clearScreen()
    numSpacesX = (TERM_WIDTH // 2) - (cellWidth // 2)
    numSpacesY = TERM_HEIGHT // 2 - HEIGHT // 2
    for x in range(numSpacesY):
        print()
    for y in range(HEIGHT):
        # push the grid right
        for i in range(numSpacesX):
            print(" ", end="")
        for x in range(WIDTH):
            # print(
            #     f"{bcolors.WARNING}" + currentCells[x][y].germChar + f"{bcolors.ENDC}",
            #     end="",
            # )
            # colourList = list(colourDict.values)
            colour = random.choice(colourList)
            # colour = colourDict["OKBLUE"]
            colourEnd = colourDict["ENDC"]
            # print(colour)
            # print(bcolors.WARNING)
            # print(
            #     bcolors.WARNING
            #     + "Warning: No active frommets remain. Continue?"
            #     + bcolors.ENDC
            # )
            cell = currentCells[x][y]
            foo = colour + cell.germChar + colourEnd
            print(foo, end="")
        print()


def printCells(currentCells):
    cells = ""
    # Print currentCells on the screen:
    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(currentCells[x][y].germChar, end="")  # Print the # or space.
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
                elif currentCells[x][y].germChar == noGerm and numNeighbors == 3:
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
                    myGerm.germChar = noGerm
                    myGerm.isAboutToDie = False
                    nextCells[x][y] = myGerm

        time.sleep(SLEEP_PERIOD)  # Add a 1-second pause to reduce flickering.
        clearScreen()


printCellGenerations()
# print_centre("Hello World")
# printCellsCenter()
