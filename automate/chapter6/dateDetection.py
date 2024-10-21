import re

# Write a regular expression that can detect dates in the DD/MM/YYYY format. Assume that the days
# range from 01 to 31, the months range from 01 to 12, and the years range from 1000 to 2999.
# Note that if the day or month is a single digit, it’ll have a leading zero.

dayRegEx = re.compile(r"(\d){2}")
dateRegEx = re.compile(r"(\d){2}")
monthRegEx = re.compile(r"(\d\d\d)-(\d\d\d-\d\d\d\d)")
yearRegEx = re.compile(r"(\d\d\d)-(\d\d\d-\d\d\d\d)")
# DD/MM/YYYY
day = "09"
date1 = "10/12/2001"
date2 = "50/12/2001"
date3 = "10/13/2001"
date4 = "10/13/xxxx"


def checkDate(regEx, dateString):
    mo1 = regEx.search(dateString)
    if mo1 is None:
        print("Not a Date")
    else:
        day = mo1.group(1)
        print("day is " + day)


checkDate(dayRegEx, day)
