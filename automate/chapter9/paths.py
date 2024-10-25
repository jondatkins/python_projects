from pathlib import Path
import os

print(Path.cwd())
print(Path.home())
print(os.path.abspath("."))
print(os.path.isabs("."))
print(os.path.isabs(os.path.abspath(".")))
