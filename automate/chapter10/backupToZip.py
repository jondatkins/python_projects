#! python3
# backupToZip.py - Copies an entire folder and its contents
# a ZIP file whose filename increments.

import zipfile, os
from pathlib import Path

home = Path.home()
cwd = Path.cwd()


def backupToZip(folder):
    # Back up dir contents into zip file
    folder = os.path.abspath(folder)
    # Figure out the filename this code should use based on
    # what files already exist.
    number = 1
    while True:
        zipFilename = os.path.basename(folder) + "_" + str(number) + ".zip"
        if not os.path.exists(zipFilename):
            break
        number = number + 1

    # TODO: Create the ZIP file.
    print(f"Creating {zipFilename}...")
    backupZip = zipfile.ZipFile(zipFilename, "w")
    # TODO: Walk the entire folder tree and compress the files in each folder.
    for foldername, subfolders, filenames in os.walk(folder):
        print(f"Adding files in {foldername}...")
        backupZip.write(foldername)
    for filename in filenames:
        newBase = os.path.basename(folder) + "_"
        if filename.startswith(newBase) and filename.endswith(".zip"):
            continue
            backupZip.write(os.path.join(foldername, filename))
    backupZip.close()
    print("Done.")


backupToZip(cwd / "foo")
