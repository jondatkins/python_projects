from pathlib import Path
import os

p = Path("/mnt/c/Users/jonda/spam.txt")
p.anchor
print(p.parent)
print(p.name)
print(p.stem)
print(p.suffix)
print(p.drive)
calcFilePath = "/mnt/c/Windows/System32/calc.exe"
print(os.path.basename(calcFilePath))
calcFilePath2 = "/mnt/c/Windows/System32/calc.exe"
print(os.path.split(calcFilePath2))
calcFilePath3 = "/mnt/c/Windows/System32/calc.exe"
print(calcFilePath3.split(os.sep))
print(os.path.getsize("/mnt/c/Windows/System32/calc.exe"))

totalSize = 0
for filename in os.listdir("/mnt/c/Windows/System32/"):
    totalSize = totalSize + os.path.getsize(
        os.path.join("/mnt/c/Windows/System32", filename)
    )
print(totalSize)
