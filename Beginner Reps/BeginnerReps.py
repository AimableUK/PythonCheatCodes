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
newArray = array(vals.typecode, (a for a in vals))  # this is right too: # (a*a for a in vals)
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
arange = arange(1, 15, 2)  # skips 2

# lospace:
arr = logspace(1, 40, 5)
print("%.2f" % arr[4])

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
arr1 = arr2  # but all still refer to one address

# 2
arr2 = arr1.view()  # the ids are different ~ but changes occur for both on assignment they are linked

# 3
arr3 = arr1.copy()  # each one is independent

# Working with Array Dimensions
multiArr = array([
    [1, 2, 3, 6, 2, 9],
    [4, 5, 6, 7, 5, 3]
])

print(multiArr)
print(multiArr.dtype)  # the type of data
print(multiArr.ndim)  # number of dimension
print(multiArr.shape)  # number of rows and columns
print(multiArr.size)  # array size

# Convert 2D to 1D
multiSingle = multiArr.flatten()

# convert 1D to 3D Array
threeD = multiArr.reshape(3, 4)

# convert 1D Array to 1 big Array with two 2D arrays
Two2DArrays = multiArr.reshape(2, 2, 3)

# MATRICES
# making a matrix
m = matrix(multiArr)
n = matrix('1 2 3 6; 4 5 6 7')

# all operations same as the array
m.max()  # the highest number

m1 = matrix('1 2 3 6; 4 5 6 7')
m2 = matrix('1 2 3 6; 4 5 6 7')
m3 = m1 + m2


# Functions
# 1
def add(x, y):
    c = x + y
    d = x - y
    return c, d


result1, result2 = add(5, 4)
print(result1, result2)


# 2
def update(lst):
    print(id(lst))

    lst[1] = 25
    print(id(lst))
    print("x ", lst)


lst = [10, 20, 30]
print(id(lst))
update(lst)
print("lst ", lst)


# 3
def person(name, age=1):
    print(name, age)


person('able', 12)
person(age='able', name=12)


# 4 summation
def sum(a, *b):
    for i in b:
        a = a + i
    print(a)


sum(5, 6, 34, 78)


# when doing **--- you must add keywords
# when doing *-- keywords not needed

# 2
# def person(name, *data):
# person('navin', 12, 'mumbai', 79768)

def person(name, **data):
    print(name)

    # 1
    print(data)

    # 2
    for i, j in data.items():
        print(i, j)


person('navin', age=12, city='mumbai', phn=79768)


# Fibonacci

def fib(n):
    a = 0
    b = 1

    if n == 1:
        print(a)

    elif n < 0:
        print("please Enter a positive number")

    elif n >= 89:
        print("Please Enter a number less than 89")

    else:
        print(a)
        print(b)

        for i in range(2, n):
            c = a + b
            a = b
            b = c

            print(c)


fib(5)


# Factorial

def fact(n):
    f = 1

    for i in range(1, n + 1):
        f = f * i

    return f


x = 5
result = fact(x)
print(result)

# lambda
f = lambda a: a * a
result = f(5)
print(result)

f1 = lambda a, b: a + b
res = f1(5, 6)
print(res)


# Decorators
# 1
def smart_div(func):
    def inner(a, b):
        if a < b:
            a, b = b, a
        return func(a, b)

    return inner


@smart_div
def div(a, b):
    print(a / b)


div(2, 4)


# 2

# Step 1: Define the decorator
def my_decorator(func):
    def wrapper():
        print("--- Before function ---")
        func()
        print("--- After function ---")

    return wrapper


# Step 2: Create the main function
def greet():
    print("I am learning Python")


# Step 3: Apply the decorator
greet = my_decorator(greet)

# Step 4: Call the decorated function
greet()

# woorking with modules: Calc module
from Calc import *

a = 9
b = 7

c = sub(a, b)
d = add(a, b)
print(c, d)


# 2

def main():
    print("Hello BOOOy")


if __name__ == '__main__':
    main()


# CLasses:
class Computer:

    def __init__(self, cpu, ram):
        self.cpu = cpu
        self.ram = ram

    def config(self):
        print("config is: ", self.cpu, self.ram)


com1 = Computer('i5', 16)
com2 = Computer("Ryzen 3", 8)

com1.config()
com2.config()


# 2

class Computer:

    def __init__(self):
        self.name = "navin"
        self.age = 20

    def update(self):
        self.age = 30

    def compare(self, other):
        if self.age == other.age:
            return True
        else:
            return False


c1 = Computer()
c1.age = 30
c2 = Computer()

if c1.compare(c2):
    print("they are same")

c1.update()

print(c1.name)
print(c2.age)


# Inner Class:
class Student:

    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno
        self.lap = self.Laptop()

    def show(self):
        print(self.name, self.rollno)

    class Laptop:

        def __init__(self):
            self.brand = 'HP'
            self.cpu = 'i5'
            self.ram = 8


s1 = Student('Navin', 2)
s2 = Student('Jenny', 3)

s1.show()

lap1 = s1.lap
lap2 = s2.lap

lap3 = Student.Laptop()


# Inheritance


class A:

    def feature1(self):
        print("feauture 1 Working")

    def feature2(self):
        print("Feature 2 Working")


class B(A):

    def feature3(self):
        print("feauture 3 Working")

    def feature4(self):
        print("Feature 4 Working")


# Multilevel inheritance
class C(B):

    def feature5(self):
        print("feauture 5 Working")


# Multiple inheritance
class D(B, C):

    def feature6(self):
        print("feauture 6 Working")


a1 = A()
a1.feature1()
a1.feature2()

b1 = B()
b1.feature1()

d1 = D()

# 2
class A:

    def __init__(self):
        print("In A init")

    def feature1(self):
        print("feauture 1 Working")

    def feature2(self):
        print("Feature 2 Working")


class B:

    def __init__(self):
        # call Class A init class
        # super().__init__()
        print("In B init")

    def feature3(self):
        print("feauture 3 Working")

    def feature4(self):
        print("Feature 4 Working")

# When you add super in init, will display class A init only
# But only when if you havent called init B too
class C(A,B):

    def __init__(self):
        # call Class A init class only
        super().__init__()
        print("In C init")

    def feature3(self):
        print("feauture 3 Working")


# When you call the objet of B it will call be init func
# But when it doesn't have init func it will call init of A
# But using Super u an call init func Of A

c = C()


# Duck Typing
class Pycharm:

    def execute(self):
        print("Compling")
        print("Running")


class Sublime:

    def execute(self):
        print("Spell Check")
        print("Convention Check")
        print("compiling")
        print("Running")


class Laptop:

    def code(self, ide):
        ide.execute()

# ide = Pycharm
ide = Sublime()

lap1 = Laptop()
lap1.code(ide)

# Operator Overloading
class Student:

    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self, other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        s3 = Student(m1, m2)

        return s3

    def __gt__(self, other):
        r1 = self.m1 + self.m2
        r2 = other.m1 + other.m2
        if r1 > r2:
            return True
        else:
            return False

    def __str__(self):
        return '{} {}'.format(self.m1, self.m2)


s1 = Student(58, 69)
s2 = Student(60, 65)

s3 = s1 + s2

if s1 > s2:
    print("s1 wins")
else:
    print("s2 wins")

a = 9
print(a)
print(s1)

# Method Overloading
class Student:

    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def sum(self, a=None, b=None, c=None):

        s = 0

        if a is not None and b is not None and c is not None:
            s = a + b + c
        elif a is not None and b is not None:
            s = a+b
        else:
            s = a

        return s


s1 = Student(58, 69)
print(s1.sum(5, 8))

# Method Overriding


class A:

    def show(self):
        print("in A Show")

class B(A):

    def show(self):
        print("in B show")



a1 = B()
a1.show()
