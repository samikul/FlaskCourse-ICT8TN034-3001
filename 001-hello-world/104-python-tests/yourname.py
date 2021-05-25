import sys

if len(sys.argv)<2:
    sys.exit("Tell me your name")

name = sys.argv[1]
print(f"Hello, { name }!")
