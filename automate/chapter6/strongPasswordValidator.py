import re

# A strong password is defined as one that is at least eight characters long, contains
# both uppercase and lowercase characters, and has at least one digit
lengthRegEx = re.compile(r"(.{8,})")
uppercaseRegEx = re.compile(r"([A-Z])")
lowercaseRegEx = re.compile(r"([a-z])")
numbersRegEx = re.compile(r"([0-9])")
upperAndLowerRegEx = re.compile(r"(?=.*[a-z])(?=.*[A-Z]).*")
# This is the first google answer, this doesn't check for upper and lower case.
googlesRegEx = re.compile(r"^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$")
# This is the answer from google, matching upper and lower case
googlesRegEx2 = re.compile(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$")

# (.{8,})
badPassword = "123"
badPassword2 = "iamtheverymodel"
badPassword3 = "iamtheverymodel4"
goodPassword = "iAmTheVeryModelOfAModernMajorGeneral2"
allCaps = "I AM SHOUTING!!!!"
lwrCase = "hello? is it me you're looking for?"
numbers = "233111112345646454646645647979789"
lowerAndUpper = "AAAsssaaaAAA"


def checkPassword(regEx, password):
    mo1 = regEx.search(password)
    if mo1 is None:
        print("{0} is not a strong password".format(password))
    else:
        print("{0} is a strong password".format(password))


# checkPassword(lengthRegEx, badPasword)
# checkPassword(lengthRegEx, goodPassword)
# checkPassword(uppercaseRegEx, allCaps)
# checkPassword(lowercaseRegEx, lwrCase)
# checkPassword(numbersRegEx, numbers)
# checkPassword(upperAndLowerRegEx, lowerAndUpper)

checkPassword(googlesRegEx, badPassword2)
