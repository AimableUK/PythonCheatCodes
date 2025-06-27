from numpy import *

arr1 = array([1, 2, 3, 4, 5])
arr2 = array([6, 1, 9, 3, 2])

print()

# adding five to each element
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
