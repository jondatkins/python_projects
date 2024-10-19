import re

phoneNumRegEx = re.compile(r"(\d\d\d)-(\d\d\d-\d\d\d\d)")

mo = phoneNumRegEx.search("My number is 415-555-4242")
if mo is None:
    print("No match")
else:
    print("Phone number found:" + mo.group(1))
    print("Phone number found:" + mo.group(2))
    print("Phone number found:" + mo.group(0))
    print("Phone number found:" + mo.group())


heroRegex = re.compile(r"Batman|Tina Fey")
mo1 = heroRegex.search("Batman and Tina Fey")
print(mo1.group())
mo2 = heroRegex.search("Tina Fey and Batman")
print(mo2.group())
