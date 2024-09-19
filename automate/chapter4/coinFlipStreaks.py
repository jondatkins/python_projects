import random

numberOfStreaks = 0
headsTails = ["H", "T"]
experimentRange = 10000
testToss = [
    "T",
    "H",
    "H",
    "H",
    "T",
    "H",
    "H",
    "H",
    "T",
    "H",
    "H",
    "H",
    "H",
    "T",
    "T",
    "H",
]
# coinTossLength = len(testToss)
coinTossLength = 100
streakLength = 6

for experimentNumber in range(experimentRange):
    # Code that creates a list of 100 'heads' or 'tails' values.
    headsOrTails = []
    for i in range(coinTossLength):
        headsOrTails.append(random.choice(headsTails))
    # headsOrTails = testToss
    # Code that checks if there is a streak of 6 heads or tails in a row.
    i = 0
    end = coinTossLength
    while i < coinTossLength:
        matchCount = 1
        y = i + 1
        end = i + streakLength
        while end < len(headsOrTails) and y < end:
            # print("ith value is: %s" % headsOrTails[i])
            # print("yth value is: %s" % headsOrTails[y])
            if headsOrTails[i] != headsOrTails[y]:
                break
            else:
                matchCount += 1
            y += 1
        if matchCount == streakLength:
            numberOfStreaks += 1
            i = i + streakLength
            # We're only looking for one streak in our run of 100 coin tosses, so break to outer loop here
            break
        else:
            i = i + 1
# numberOfStreaks / 10000 * 100 is the same as numberOfStreaks / 100
print("Chance of streak: %s%%" % (numberOfStreaks / coinTossLength))
print("Number of streaks: %s" % numberOfStreaks)
