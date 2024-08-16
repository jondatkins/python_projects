import time

print(
    'Press Enter to begin. Afterward, press ENTER to "click" the stopwatch. Press Ctrl-C to quit.'
)
input()
print("Started")
startTime = time.time()
lastTime = startTime
lapNum = 1

try:
    while True:
        input()
        lapTime = round(time.time() - lastTime, 2)
        totalTime = round(time.time() - startTime, 2)
        print("Lap #%s: %s (%s)" % (lapNum, totalTime, lapTime), end="")
except KeyboardInterrupt:
    print("\nDone")
