from pathlib import Path
import os

p = Path("/mnt/c/Users/jonda/desktopfiles/")
print(p.glob("*"))
print(list(p.glob("*")))
print(list(p.glob("*.txt")))
