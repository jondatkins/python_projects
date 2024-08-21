import time
import subprocess

# for i in range(10):
#     print(i)
#     time.sleep(1)
# timeLeft = 60
# while timeLeft > 0:
#     print(timeLeft, end="")
#     time.sleep(1)
#     timeLeft -= 1
# file = "mixkit-classic-alarm-995.wav"
# os.system("paplay " + file)
timeLeft = 10
while timeLeft > 0:
    # Add flush=True here so that each number is printed every second,
    # rather than all at the end of the countdown
    print(timeLeft, end=" ", flush=True)
    time.sleep(1)
    timeLeft = timeLeft - 1
subprocess.run(["paplay", "mixkit-classic-alarm-995.wav"])
