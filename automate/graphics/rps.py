import sys
import random
from enum import Enum


class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


print("")
player = "-1"
while True:
    playerchoice = input(
        "Enter... \n1 for Rock,\n2 for Paper, or \n3 for Scissors:\n\n"
    )
    try:
        player = int(playerchoice)
    except Exception as ex:
        print("Please enter a number from 1 to 3.")
        print(ex)
        continue
    if player < 1 or player > 3:
        print("You must enter 1, 2 or 3.")
        continue
    break


computerchoice = random.choice("123")

computer = int(computerchoice)

print("")
print("You chose " + str(RPS(player)).replace("RPS.", "") + ".")
print("Python chose " + str(RPS(computer)).replace("RPS.", "") + ".")
print("")

if player == 1 and computer == 3:
    print("🥂 You win!")
elif player == 2 and computer == 1:
    print("🥂 You win!")
elif player == 3 and computer == 2:
    print("🥂 You win!")
elif player == computer:
    print("😄 Tie game!")
else:
    print("🐍Python wins!")
