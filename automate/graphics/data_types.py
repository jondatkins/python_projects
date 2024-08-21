import math

first = "python tutorial for beginners"
print(first.startswith("t"))
print(first.endswith("s"))

# Booleans
myvalue = True
x = bool(False)

# Numeric data types

# integer type
price = 100
best_price = int(80)
print(type(price))
print(isinstance(best_price, int))

# float type
gpa = 3.28
y = float(1.14)
print(type(gpa))

# complex type
comp_value = 5 + 3j
print(type(comp_value))
print(type(comp_value.real))
print(type(comp_value.imag))

print(abs(gpa))
print(round(gpa))
print(round(gpa, 1))

print(math.pi)
print(math.sqrt(64))
print(math.ceil(gpa))
print(math.floor(gpa))

# Casting a string to a number
zipcode = "1001"
zip_value = int(zipcode)
print(type(zip_value))

# Error if you attempt to cast incorrect data
# zip_value = int("New York")
