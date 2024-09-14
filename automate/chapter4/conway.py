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
noGerm = " - "
goingToDie = " X "
currentCells = []

# Get the width and height of the terminal
rows, columns = os.popen("stty size", "r").read().split()
TERM_WIDTH = int(columns)
TERM_HEIGHT = int(rows)
# The widht and height of the grid in cells
WIDTH = 10
HEIGHT = 10


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
        self.isAboutToRevive = False
        self.germChar = germ
        self.noGermChar = germ


# Start process with random grid of cells


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


colourList = list(colourDict.values())
# colourList.remove("\033[0m")


def randomCellsGenerator():
    # Create a list of list for the cells:
    randCells = []
    for x in range(WIDTH):
        column = []  # Create a new column.
        for y in range(HEIGHT):
            if random.randint(0, 1) == 0:
                # glider pattern
                # if (x, y) in ((1, 0), (2, 1), (0, 2), (1, 2), (2, 2)):
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


nextCells = randomCellsGenerator()


def getCenterStringX():
    # push the grid right
    # widthSpacerString = ""
    numSpacesX = (TERM_WIDTH // 2) - (cellWidth // 2)
    # for i in range(numSpacesX):
    #     # print(" ", end="")
    #     widthSpacerString += " "
    # return widthSpacerString
    for i in range(numSpacesX):
        print(" ", end="")


def getCenterStringX2():
    # push the grid right
    widthSpacerString = ""
    numSpacesX = (TERM_WIDTH // 2) - (cellWidth // 2)
    for i in range(numSpacesX):
        # print(" ", end="")
        widthSpacerString += " "
    return widthSpacerString


def getCenterStringY():
    numSpacesY = TERM_HEIGHT // 2 - HEIGHT // 2
    for x in range(numSpacesY):
        print()


def getCenterStringY2():
    numSpacesY = TERM_HEIGHT // 2 - HEIGHT // 2
    carrReturn = ""
    for x in range(numSpacesY):
        carrReturn += "\n"
    return carrReturn


# gets a random colour for each cell in the grid.
def getColouredCharacter(germChar):
    colour = random.choice(colourList)
    colourEnd = colourDict["ENDC"]
    foo = colour + germChar + colourEnd
    return foo


# prints cell grid in centre of terminal
def printCellsCenter(currentCells, markedCells=False):
    clearScreen()
    # getCenterStringY()
    cells = ""
    newLines = getCenterStringY2()
    print(newLines, end="")
    for y in range(HEIGHT):
        cells += getCenterStringX2()
        for x in range(WIDTH):
            cell = currentCells[x][y]
            germChar = cell.germChar
            # if cell.isAboutToDie:
            #     germChar = goingToDie
            foo = getColouredCharacter(germChar)
            cells += foo
        cells += "\n"
    print(cells)


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


def getInput():
    key = input()
    if key == "q":
        sys.exit()


def mainLoop():
    while True:
        try:
            currentCells = copy.deepcopy(nextCells)
            printCellsCenter(currentCells)
            liveOrDieDecider(currentCells)
            # time.sleep(SLEEP_PERIOD)  # Add a 1-second pause to reduce flickering.
            # press return to continue
            getInput()
            # print marked cells here?
            printCellsCenter(currentCells, True)
            getInput()
            clearScreen()
            # press any key to continue
        except KeyboardInterrupt:
            print("Bye")
            sys.exit()


# Works out which cells live and die
def liveOrDieDecider(currentCells):

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
            if currentCells[leftCoord][aboveCoord].isAlive:
                numNeighbors += 1  # Top-left neighbor is alive.
            if currentCells[x][aboveCoord].isAlive:
                numNeighbors += 1  # Top neighbor is alive.
            if currentCells[rightCoord][aboveCoord].isAlive:
                numNeighbors += 1  # Top-right neighbor is alive.
            if currentCells[leftCoord][y].isAlive:
                numNeighbors += 1  # Left neighbor is alive.
            if currentCells[rightCoord][y].isAlive:
                numNeighbors += 1  # Right neighbor is alive.
            if currentCells[leftCoord][belowCoord].isAlive:
                numNeighbors += 1  # Bottom-left neighbor is alive.
            if currentCells[x][belowCoord].isAlive:
                numNeighbors += 1  # Bottom neighbor is alive.
            if currentCells[rightCoord][belowCoord].isAlive:
                numNeighbors += 1  # Bottom-right neighbor is alive.

            # Set cell based on Conway's Game of Life rules:
            if currentCells[x][y].isAlive and (numNeighbors == 2 or numNeighbors == 3):
                # Living cells with 2 or 3 neighbors stay alive:
                nextCells[x][y].isAlive = True
                nextCells[x][y].germChar = germ
                nextCells[x][y].isAboutToDie = False
                # nextCells[x][y].isAboutToRevive = True
            elif numNeighbors == 3:
                # Dead cells with 3 neighbors become alive:
                nextCells[x][y].isAlive = True
                nextCells[x][y].germChar = germ
                nextCells[x][y].isAboutToDie = False
                # nextCells[x][y].isAboutToRevive = True
            # if not alive, or about to be born,            the cell
            else:
                nextCells[x][y].isAlive = False
                nextCells[x][y].germChar = noGerm
                nextCells[x][y].isAboutToDie = True


mainLoop()
