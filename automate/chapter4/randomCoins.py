import random

for experimentNumber in range(10000):
    # Code that creates a list of 100 'heads' or 'tails' values.
    flips = []
    for i in range(100):
        if random.randint(0, 1):
            flips.append("H")
        else:
            flips.append("T")

    print("".join(flips))
