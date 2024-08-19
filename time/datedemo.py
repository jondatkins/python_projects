import datetime
import time

print(datetime.datetime.fromtimestamp(1000000))
print(datetime.datetime(1970, 1, 12, 5, 46, 40))
print(datetime.datetime.fromtimestamp(time.time()))
print(datetime.datetime(2019, 10, 21, 16, 30, 0, 604980))


halloween2019 = datetime.datetime(2019, 10, 31, 0, 0, 0)
newyears2020 = datetime.datetime(2020, 1, 1, 0, 0, 0)
oct31_2019 = datetime.datetime(2019, 10, 31, 0, 0, 0)
print(halloween2019 == oct31_2019)
print(halloween2019 > newyears2020)
print(newyears2020 > halloween2019)
print(newyears2020 != oct31_2019)


delta = datetime.timedelta(days=11, hours=10, minutes=9, seconds=8)
print(delta.days, delta.seconds, delta.microseconds)
print(delta.total_seconds())
print(str(delta))


dt = datetime.datetime.now()
print(dt)
print(datetime.datetime(2018, 12, 2, 18, 38, 50, 636181))
thousandDays = datetime.timedelta(days=1000)
print(dt + thousandDays)
print(datetime.datetime(2021, 8, 28, 18, 38, 50, 636181))


oct21st = datetime.datetime(2019, 10, 21, 16, 29, 0)
aboutThirtyYears = datetime.timedelta(days=365 * 30)
print(oct21st)
print(datetime.datetime(2019, 10, 21, 16, 29))
print(oct21st - aboutThirtyYears)
print(datetime.datetime(1989, 10, 28, 16, 29))
print(oct21st - (2 * aboutThirtyYears))
print(datetime.datetime(1959, 11, 5, 16, 29))
