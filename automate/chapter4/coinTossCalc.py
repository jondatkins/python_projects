import random

numberOfStreaks = 0
headsTails = ["H", "T"]
coinTossLength = 100

headsOrTails = []
for i in range(coinTossLength):
    headsOrTails.append(random.choice(headsTails))
# Code that checks if there is a streak of 6 heads or tails in a row.
hCount = 0
tCount = 0
for i in range(coinTossLength):
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
