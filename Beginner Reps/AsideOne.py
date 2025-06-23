import sys

if len(sys.argv) != 3:
    print("Usage: python add.py <number1> <number2>")
    sys.exit(1)

try:
    x = int(sys.argv[1])
    y = int(sys.argv[2])
    print(x + y)
except ValueError:
    print("Both arguments must be integers.")
