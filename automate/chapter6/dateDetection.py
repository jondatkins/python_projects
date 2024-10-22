import re

# Write a regular expression that can detect dates in the DD/MM/YYYY format. Assume that the days
# range from 01 to 31, the months range from 01 to 12, and the years range from 1000 to 2999.
# Note that if the day or month is a single digit, it’ll have a leading zero.
dayRegExString = r"(0[1-9]|1[0-9]|2[0-9]|3[0-1])"
dayRegExString2 = r"(0[1-9]|[12][0-9]|3[01])"
monthRegExString = r"(0[1-9]|1[0-2])"
yearRegExString = r"([1-2][0-9][0-9][0-9])"
dayRegEx = re.compile(dayRegExString)
monthRegEx = re.compile(monthRegExString)
yearRegEx = re.compile(yearRegExString)
dayRegEx2 = re.compile(dayRegExString2)

leapYears = [
    1804,
    1808,
    1812,
    1816,
    1820,
    1824,
    1828,
    1832,
    1836,
]
normalYears = [1700, 1800, 1900, 2100]

dateRegEx = re.compile(
    r"""(
    (0[1-9]|1[0-9]|2[0-9]|3[0-1]) # days 00 - 31
    /                    # separator
    (0[1-9]|1[0-2])
    /                    # separator
    ([1-2][0-9][0-9][0-9])
    )""",
    re.VERBOSE,
)

dates = ["01/09/2999", "2/09/2000", "31/99/2000", "11/11/999", "11/11/3001"]
dates2 = ["01/09/2999", "12/09/2000", "31/09/2000"]
badDates = ["31/04/2000", "31/02/2020", "31/04/2021"]
# DD/MM/YYYY

days = [
    "09",
    "9",
    "99",
    "xx",
    "y",
    "23",
    "13",
    "31",
]
months = ["01", "12", "09", "2", "77", "foo"]
years = ["1000", "200", "2999", "999", "xyz"]


def checkDate(regEx, dateString, dayMonthYear):
    mo1 = regEx.search(dateString)
    dateData = {}
    if mo1 is None:
        print(dateString + " is not a " + dayMonthYear)
    else:
        # day = mo1.group(1)
        dateData = {"day": mo1.group(2), "month": mo1.group(3), "year": mo1.group(4)}
        # print(dayMonthYear + " is " + day)
    return dateData


# April, June, September, and November
# have 30 days, February has 28 days, and the rest of the months have 31 days.
# February has 29 days in leap years. Leap years are every year evenly divisible by 4,
# except for years evenly divisible by 100, unless the year is also evenly divisible by 400.
# Note how this calculation makes it impossible to make a reasonably sized
# regular expression that can detect a valid date.
def validateDates(dateData):
    day = int(dateData["day"])
    month = int(dateData["month"])
    year = int(dateData["year"])

    # 04,06,09,11
    if month == 4 or month == 6 or month == 9 or month == 11:
        if day > 30:
            print("Month " + str(month) + " has too many days " + str(day))
            return False
    elif month == 2:
        if isLeapYear(year) and day > 29:
            return False
        elif day > 28:
            print("Month " + str(month) + " has too many days " + str(day))
            return False
    else:
        if day > 31:
            print("Month " + str(month) + " has too many days " + str(day))
            return False


def isLeapYear(y):
    year = int(y)
    if year % 4 == 0 and not year % 100 == 0 or year % 400 == 0:
        # print("My name is {0} and I am {1} years old".format(name, age))
        print("this year {0} is a leap year".format(year))
        return False
    else:
        print("this year {0} is not a leap year".format(year))
        return True


# for d in days:
#     checkDate(dayRegEx2, d, "day")
#
# for m in months:
#     checkDate(monthRegEx, m, "month")
#
# for y in years:
#     checkDate(yearRegEx, y, "year")

for d in badDates:
    dateData = checkDate(dateRegEx, d, "date")
    validateDates(dateData)

# for ly in leapYears:
#     isLeapYear(ly)

# for y in normalYears:
#     isLeapYear(y)
