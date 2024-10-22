import re

# A strong password is defined as one that is at least eight characters long, contains
# both uppercase and lowercase characters, and has at least one digit
passwordRegExString = r"(0[1-9]|1[0-9]|2[0-9]|3[0-1])"
lengthRegEx = re.compile(r"(.{8,})")
uppercaseRegEx = re.compile(r"([A-Z])")
lowercaseRegEx = re.compile(r"([a-z])")
numbersRegEx = re.compile(r"([0-9])")
passwordRegEx = re.compile(passwordRegExString)
# (.{8,})
badPasword = "123"
goodPassword = "iAmTheVeryModelOfAModernMajorGeneral2"
allCaps = "I AM SHOUTING!!!!"
lwrCase = "hello? is it me you're looking for?"
numbers = "233111112345646454646645647979789"


def checkPassword(regEx, password):
    mo1 = regEx.search(password)
    if mo1 is None:
        print("{0} is not a strong password".format(password))
    else:
        print("{0} is a strong password".format(password))


checkPassword(lengthRegEx, badPasword)
checkPassword(lengthRegEx, goodPassword)
checkPassword(uppercaseRegEx, allCaps)
checkPassword(lowercaseRegEx, lwrCase)
checkPassword(numbersRegEx, numbers)
