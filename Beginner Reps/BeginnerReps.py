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

# If Statement:
x = 3
r = x % 2

if r == 0:
    print("Even")
elif r == 1:
    print("Odd")
    if x < 5:
        print("Great")
    else:
        print("Poor Boy")

else:
    print("Prime")

print("bye")

# LOOPS

# WHILE Loop:

i = 1

while i <= 5:
    print("Great ", end="")
    j = 1
    while j <= 4:
        print("rocks ", end="")
        j = j + 1

    i = i + 1
    print()

# FOR Loop
# Looping in the Word
y = 'NAVIN'
for i in y:
    print(i)

# Looping in List
x = ['navin', 65, 2.5]
for i in x:
    print(i)
# same as above
for i in [2, 6, 'Paul']:
    print(i)

# Range
# 11: Starting Point
# 21: Ending Point
# 3: Interval
for i in range(11, 21, 3):
    print(i)

# reverse order
for i in range(20, 10, -1):
    print(i)

# Condition in range:
for i in range(1, 21):  # 1: Starting Point 21: Ending Point
    if i % 5 != 0:
        print(i)

# Break, Continue, Pass Statements

# Break Statement
av = 10
x = int(input("How many Candies you want"))
i = 1

while i <= x:
    if i > av:
        print("Out of Stock")
        break
    print("Candy")
    i += 1
print("Bye")

# Continue statement
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        continue
    print(i)
print("Bye")

# PASS: Means noe Code Ignore it
for i in range(1, 101):
    if i % 2 != 0:
        pass
    else:
        print(i)
print("Bye")

# Certain Pattern:
# 1:
for i in range(4):
    for j in range(4):
        print("# ", end="")
    print()

# 2:
for i in range(5):
    for j in range(i + 1):
        print("# ", end="")
    print()

# 3:
for i in range(5):
    for j in range(4 - i):
        print("# ", end="")
    print()

# 4:
for i in range(4, 0, -1):
    for j in range(i, 5):
        print(j, end="")
    print()
