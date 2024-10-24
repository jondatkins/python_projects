import re

whiteSpaces1 = "   strip my spaces   "
strpOtherChars = "strip thexcharactexr x. xxxx"

phoneNumRegEx = re.compile(r"(\d\d\d)-(\d\d\d-\d\d\d\d)")

mo = phoneNumRegEx.search("My number is 415-555-4242")


def strip(stringToStrip, charToStrip):
    if len(charToStrip) == 0:
        charToStrip = r"\s"
    localString = stringToStrip
    spaceRegEx = re.compile(charToStrip)
    localString = spaceRegEx.sub("", localString)
    return localString


testString = strip(whiteSpaces1, "")
testString2 = strip(strpOtherChars, "x")
print(testString, end="")
print("end of first string")
print(testString2)
