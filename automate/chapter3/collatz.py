import sys
import time


def collatz(number):
    if number % 2 == 0:
        print(number // 2)
        return number // 2
    else:
        print(3 * number + 1)
        return 3 * number + 1


print("Enter a number:")
number = 1
try:
    number = int(input())
    if number < 0:
        print("number can't be negative")
        # sys.exit()
        raise ValueError("foo")

except ValueError:
    print("Please enter a positive integer")
    # sys.exit()
while number != 1:
    number = collatz(number)
    time.sleep(1)
