from pathlib import Path

sonnetFile = open(Path.cwd() / "sonnet29.txt")
sonnet = sonnetFile.readlines()
print(sonnet)
