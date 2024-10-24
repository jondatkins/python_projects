import pyinputplus as pyip

ingredients = {
    "wheat": 20,
    "white": 60,
    "sourdough": 100,
    "chicken": 200,
    "turkey": 180,
    "ham": 200,
    "cheddar": 10,
    "swiss": 30,
    "mozzarella": 15,
}
breadType = pyip.inputMenu(["wheat", "white", "sourdough"])
proteinType = pyip.inputMenu(["chicken", "turkey", "ham"])
isCheese = pyip.inputYesNo("Would you like cheese?")
cheeseType = ""
if isCheese:
    cheeseType = pyip.inputMenu(["cheddar", "swiss", "mozzarella"])
mayo = pyip.inputYesNo("Would you like mayo?")
mustard = pyip.inputYesNo("Would you like mustard?")
lettuce = pyip.inputYesNo("Would you like lettuce?")
tomato = pyip.inputYesNo("Would you like tomato?")

numSandwiches = pyip.inputInt("How many sandwiches would you like?", greaterThan=1)
cheeseCost = 0
print(
    f"You ordered {numSandwiches} x {breadType} bread {proteinType} sandwich with {cheeseType}"
)
if isCheese:
    cheeseCost = ingredients[cheeseType]
    print(f"You ordered {cheeseType} cheese")
print(
    f"You will have mayo {mayo} mustard {mustard} lettuce {lettuce} and tomato {tomato}"
)
breadCost = ingredients[breadType]
proteinCost = ingredients[proteinType]
cost = breadCost + proteinCost + cheeseCost
cost = cost * numSandwiches
print(f"Your order costs {cost}")
