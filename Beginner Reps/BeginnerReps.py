import math
from numpy import *


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

# FOR...Else
nums = [12, 16, 18, 21, 26]

for num in nums:

    if num % 5 == 0:
        print(num)
        break
else:
    print("not found")

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
for i in range(1, 21):  # 1: Starting Point 21: Ending Point - 20
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

# PASS: Means no Code ~ Ignore it
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

# Prime Number:
num = 7

for i in range(2, num):
    if num % i == 0:
        print("not prime")
        break
else:
    print("Prime")

# array:

from array import *

vals = array('i', [55, 9, 8, 4, 2])

print(vals)  # all array list
print(vals.buffer_info())  # (1786002774320, 5) (address, size)
print(vals.reverse())  # to reverse
print(vals[0])  # print the number on that index

# Printing array values
# 1
for i in range(len(vals)):
    print(vals[i])

# 2
for e in vals:
    print(e)

# Creating new array from the existing One
newArray = array(vals.typecode, (a for a in vals)) # this is right too: # (a*a for a in vals)
# 1
for e in newArray:
    print(e)
# 2

i = 0
while i < len(newArray):
    print(newArray[i])
    i += 1

# array functions
# Searching
arr = array('i', [])

n = int(input("Enter the length of the array: "))


for i in range(n):
    x = int(input("Enter the Value: "))
    arr.append(x)

print(arr)

val = int(input("Enter the value of search: "))

# 1
k = 0
for e in arr:
    if e == val:
        print(k)
        break

    k += 1

# 2
print(arr.index(val))

# linspace:
lin = linspace(0, 15, 16)

# arange:
arange = arange(1, 15, 2) # skips 2

# lospace:
arr = logspace(1, 40, 5)
print("%.2f" %arr[4])

arra = ones(5)

# COPYING ARRAY
arr1 = array([1, 2, 3, 4, 5])
arr2 = array([6, 1, 9, 3, 2])


arr1 + 5

# array addition
arr1 + arr2

# ....
sin(arr1)  # to find the sin and other math functions
sqrt(arr2)
max(arr2)  # the large element
concatenate([arr1, arr2])

# copying an array
# 1
arr1 = arr2 # but all still refer to one address

# 2
arr2 = arr1.view() # the ids are different ~ but changes occur for both on assignment they are linked

# 3
arr3 = arr1.copy() # each one is independent

