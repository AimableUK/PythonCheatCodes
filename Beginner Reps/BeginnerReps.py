import math

# 1. you can also use the alias like: import math as m
# then to access it : m.sqrt();

# 2. importing only one from math :
# from math import sqrt
# then to access it type: sqrt();

# Square root
print(math.sqrt(25))

# rounding Off
print(math.floor(2.9))
print(math.ceil(2.2))
# Powering
print(math.pow(3, 2))
# Constant
print(math.pi)

# swapping
a = 5
b = 6
a, b = b, a
print(a, b)

# INPUTS

# Getting the User Input
x = input("Enter 1st Number")
y = input("Enter 2nd Number")

z = x + y
print(z)

# characters
ch = input("Enter a character: ")

print(ch[0])

# Evaluating the numbers with the expressions
# eg: 3+6-2
result = eval(input("Enter an expr: "))

print(result)

# ARGV Done in the CMD Shell:
import sys

if len(sys.argv) != 3:
    print("Usage: python BeginnerReps.py <number1> <number2>")
    sys.exit(1)

try:
    x = int(sys.argv[1])
    y = int(sys.argv[2])
    print(x + y)
except ValueError:
    print("Both arguments must be integers.")
