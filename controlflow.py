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
