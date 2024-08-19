import datetime
import time

someDate = datetime.datetime(2024, 8, 19, 17, 47, 0)
while datetime.datetime.now() < someDate:
    print("sleeping")
    time.sleep(1)
print("awake")


oct21st = datetime.datetime(2019, 10, 21, 16, 29, 0)
print(oct21st.strftime("%Y/%m/%d %H:%M:%S"))
print(oct21st.strftime("%I:%M %p"))
print(oct21st.strftime("%B of '%y"))


print(datetime.datetime.strptime("October 21, 2019", "%B %d, %Y"))
print(datetime.datetime(2019, 10, 21, 0, 0))
print(datetime.datetime.strptime("2019/10/21 16:29:00", "%Y/%m/%d %H:%M:%S"))
print(datetime.datetime(2019, 10, 21, 16, 29))
print(datetime.datetime.strptime("October of '19", "%B of '%y"))
print(datetime.datetime(2019, 10, 1, 0, 0))
print(datetime.datetime.strptime("November of '63", "%B of '%y"))
print(datetime.datetime(2063, 11, 1, 0, 0))
