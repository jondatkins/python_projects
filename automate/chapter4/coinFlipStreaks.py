import random

numberOfStreaks = 0
headsTails = ["H", "T"]
# experimentRange = 10000
experimentRange = 1
testToss = [
    "H",
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
# streakLength = 3

# You can use the testToss list to debug, by uncommenting lines with testToss in them. You can also shorten the streak length to make life easier

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
        # loop over each potential streak
        while end < len(headsOrTails) and y < end:
            # if i and y are different, there's no streak, so break to outer loop and start again
            if headsOrTails[i] != headsOrTails[y]:
                break
            else:
                matchCount += 1
            y += 1
        if matchCount == streakLength:
            numberOfStreaks += 1
            # This index update makes sense if we are counting all the streaks in a run of coin tosses.
            # However, we break to the outer for loop here, so there's no reason to do this.
            # i = i + streakLength
            # We're only looking for one streak in our run of 100 coin tosses, so break to outer loop here
            break
        else:
            # increment i for inner loop where no match is found
            i = i + 1
# numberOfStreaks / 10000 * 100 is the same as numberOfStreaks / 100
print("Chance of streak: %s%%" % (numberOfStreaks / coinTossLength))
print("Number of streaks: %s" % numberOfStreaks)
