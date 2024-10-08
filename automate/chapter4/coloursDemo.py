import sys

from termcolor import colored, cprint

foo = ["blue", "red", "green"]
# text = colored("Hello, World!", "red", attrs=["reverse", "blink"])
text = colored("Hello, World!", "red")
print(text)
cprint("Hello, World!", "green", "on_red")

print_red_on_cyan = lambda x: cprint(x, foo[1], "on_cyan")
print_red_on_cyan("Hello, World!")
print_red_on_cyan("Hello, Universe!")

for i in range(10):
    cprint(i, "magenta", end=" ")

cprint("Attention!", "red", attrs=["bold"], file=sys.stderr)
