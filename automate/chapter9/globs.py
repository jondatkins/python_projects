from pathlib import Path
import os

p = Path("/mnt/c/Users/jonda/desktopfiles/")
print(p.glob("*"))
print(list(p.glob("*")))
print(list(p.glob("*.txt")))
winDir = Path("/home/jon/")
notExistsDir = Path("C:/Windows")
print(winDir.exists())
