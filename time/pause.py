import datetime
import time

someDate = datetime.datetime(2024, 8, 19, 10, 59, 0)
while datetime.datetime.now() < someDate:
    time.sleep(1)
