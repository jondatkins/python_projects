import time
import threading

print("Start of program")


def takeNap():
    time.sleep(5)
    print("Wake up!")


threadObj = threading.Thread(target=takeNap)
threadObj.start()

print("End of program")
