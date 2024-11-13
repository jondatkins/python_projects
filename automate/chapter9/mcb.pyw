#! python3
# mcb.pyw - Saves and loads pieces of text to the clipboard.
# Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword.
#        py.exe mcb.pyw <keyword> - Loads keyword to clipboard.
#        py.exe mcb.pyw list - Loads all keywords to clipboard.
#        py.exe mcb.pyw delete <keyword> - Deletes keyword from the shelf.
#        py.exe mcb.pyw delete - Deletes all keywords

import shelve
import pyperclip
import sys

mcbShelf = shelve.open("mcb")

# TODO: Save clipboard content.
if len(sys.argv) == 3:
    if sys.argv[1].lower() == "save":
        mcbShelf[sys.argv[2]] = pyperclip.paste()
    if sys.argv[1].lower() == "delete":
        print("deleting shelf file for " + sys.argv[2])
        del mcbShelf[sys.argv[2]]
elif len(sys.argv) == 2:
    # TODO: List keywords and load content.
    if sys.argv[1].lower() == "list":
        pyperclip.copy(str(list(mcbShelf.keys())))
        print(str(list(mcbShelf.keys())))
        print(str(list(mcbShelf.values())))
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])
        print(mcbShelf[sys.argv[1]])
    elif sys.argv[1].lower() == "delete":
        print("deleting keys / values")
        for key in mcbShelf.keys():
            del mcbShelf[key]
        print(str(list(mcbShelf.keys())))
        print(str(list(mcbShelf.values())))
mcbShelf.close()
