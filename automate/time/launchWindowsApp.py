from re import sub
import subprocess

# This works on wsl 2, where the 'C' drive is at /mnt/c
paintProc = subprocess.Popen("/mnt/c/Program Files/ImageGlass/ImageGlass.exe")
