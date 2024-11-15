import zipfile, os

from pathlib import Path

p = Path.cwd()
exampleZip = zipfile.ZipFile(p / "foo_1.zip")
print(exampleZip.namelist())
# ['spam.txt', 'cats/', 'cats/catnames.txt', 'cats/zophie.jpg']
spamInfo = exampleZip.getinfo("eggs.txt")
spamInfo.file_size
spamInfo.compress_size

print(
    f"Compressed file is {round(spamInfo.file_size / spamInfo.compress_size, 2)}x smaller!"
)
# 'Compressed file is 3.63x smaller!'
exampleZip.close()
