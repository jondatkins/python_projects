import time
import subprocess
import os

for i in range(10):
    print(i)
    time.sleep(1)
subprocess.run(["paplay", "mixkit-classic-alarm-995.wav"])
# file = "mixkit-classic-alarm-995.wav"
# os.system("paplay " + file)
