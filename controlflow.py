from enum import Enum

# Measure some strings:
words = ["cat", "window", "defenestrate"]
for w in words:
    print(w, len(w))
# Create a simple collection
users = {"Hans": "active", "Eleonore": "inactive", "foo": "active"}

print(users)
# Strategy: Iterate over a copy
for user, status in users.copy().items():
    if status == "inactive":
        del users[user]

print(users)
# Strategy: Create a new collection
active_users = {}
for user, status in users.items():
    if status == "active":
        active_users[user] = status

print(active_users)

# The range function
for i in range(5):
    print(i)

print(list(range(5, 10)))
print(list(range(0, 10, 3)))
print(list(range(-10, -100, -30)))

a = ["Mary", "had", "a", "little", "lamb"]
for i in range(len(a)):
    print(i, a[i])

print(range(10))

# else statements in for loops
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, "equals", x, "*", n // x)
            break
    else:
        print(n, "is a prime number")

for num in range(2, 10):
    if num % 2 == 0:
        print("Found an even number")
        continue
    print("Found an odd number", num)

# The pass statement does nothing, e.g.
# while True:
#     pass  # Busy-wait for keyboard interrupt (Ctrl+c)


# Commonly used to create a minimal class / placeholder
class MyEmptyClass:
    pass


def initlog(*args):
    pass  # ToDo remember todo!!!


# match statements
# Similar to a switch statement


def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case _:
            return "We're Doomed! Doomed!!!"


print(http_error(400))
print(http_error(404))
print(http_error(418))
print(http_error(419))


def error_example(status):
    match status:
        case 401 | 403 | 404:
            return "Not allowed"


print(error_example(404))
print(error_example(401))
print(error_example(403))


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def where_is(point):
    # point is an (x, y) tuple
    match point:
        case (0, 0):
            print("Origin")
        case (0, y):
            print(f"Y={y}")
        case (x, 0):
            print(f"X={x}")
        case (x, y):
            print(f"X={x}, Y={y}")
        case _:
            raise ValueError("Not a point")


class Color(Enum):
    RED = "red"
    GREEN = "green"
    BLUE = "blue"


# color = Color(input("Enter your choice of 'red', 'blue' or 'green': "))
#
# match color:
#     case Color.RED:
#         print("I see red!")
#     case Color.GREEN:
#         print("Grass is green")
#     case Color.BLUE:
#         print("I'm feeling the blues :(")
#


def fib(n):  # write Fibonacci series up to n
    """Print a Fibonacci series up to n."""
    a, b = 0, 1
    while a < n:
        print(a, end=" ")
        a, b = b, a + b
    print()


# Now call the function we just defined:
fib(2000)

print(fib)
f = fib
f(100)


def fib2(n):  # return Fibonacci series up to n
    """Return a list containing the Fibonacci series up to n."""
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)  # see below
        a, b = b, a + b
    return result


f100 = fib2(100)  # call it
print(f100)  # write the result
