import re

greedyHaRegex = re.compile(r"(Ha){3,5}")
nongreedyHaRegex = re.compile(r"(Ha){3,5}?")
# Pattern will match 3 to 5 'Ha's. If there are 5 'Ha's, it returns that match, i.e.
# the matching is greedy by default.
mo1 = greedyHaRegex.search("HaHaHaHaHa")
if mo1 is not None:
    print(mo1.group())
mo2 = nongreedyHaRegex.search("HaHaHaHaHa")
if mo2 is not None:
    print(mo2.group())
consonantRegex = re.compile(r"[^aeiouAEIOU]")
print(consonantRegex.findall("Robocopo eats baby food. BABY FOOD"))

nameRegex = re.compile(r"First Name: (.*) Last Name: (.*)")
mo3 = nameRegex.search("First Name: Al Last Name: Sweigart")
if mo3 is not None:
    print(mo3.group(1))
    print(mo3.group(2))
