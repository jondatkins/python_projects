import time
import sys

sys.set_int_max_str_digits(0)


def calcProd():
    product = 1
    for i in range(1, 100):
        product = product * i
    return product


startTime = time.time()
prod = calcProd()
endTime = time.time()
print("The result is %s digits long." % (len(str(prod))))
print("It took %s seconds to calculate." % (endTime - startTime))
print(time.ctime())
thisMoment = time.time()
print(time.ctime(thisMoment))

for i in range(3):
    print("Tick")
    time.sleep(1)
    print("Tock")
    time.sleep(1)
