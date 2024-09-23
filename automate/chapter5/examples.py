import pprint

message = "It was a bright cold day in April, and the clocks were striking thirteen."
count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1

pprint.pprint(count)


spam = {"name": "Pooka", "age": 5}
if "color" not in spam:
    spam["color"] = "black"
print(spam["color"])

# spam = {"bar": 100}
# print(spam["foo"])
# print(spam.get("foo", 0))
spam = {"name": "Pooka", "age": 5}
spam.setdefault("color", "black")
print(spam["color"])
print(spam)
