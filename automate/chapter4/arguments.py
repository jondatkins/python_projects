# argv.py
import sys

print(f"Name of the script      : {sys.argv[0]=}")
print(f"Arguments of the script : {sys.argv[1:]=}")

print(sys.argv)
sys.argv.pop()
print(sys.argv)
