import random

numberOfStreaks = 0
headsTails = ["H", "T"]
experimentRange = 1000
coinTossLength = 100
for experimentNumber in range(experimentRange):
    # Code that creates a list of 100 'heads' or 'tails' values.
    headsOrTails = []
    for i in range(coinTossLength):
        headsOrTails.append(random.choice(headsTails))
    # Code that checks if there is a streak of 6 heads or tails in a row.
    hCount = 0
    tCount = 0
    for i in range(100):
        if headsOrTails[i] == "H":
            hCount += 1
        if hCount == 6:
            numberOfStreaks += 1
            hCount = 0
        if headsOrTails[i] == "T":
            tCount += 1
        if tCount == 6:
            numberOfStreaks += 1
            tCount = 0
    print("Chance of streak: %s%%" % (numberOfStreaks / 100))
    numberOfStreaks = 0
