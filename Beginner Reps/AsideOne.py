

# Looping in the Word
y = 'NAVIN'
for i in y:
    print(i)

# Looping in List
x = ['navin', 65, 2.5]
for i in x:
    print(i)
# same as above
for i in [2,6,'Paul']:
    print(i)

# Range
# 11: Starting Point
# 21: Ending Point
# 3: Interval
for i in range(11,21,3):
    print(i)

# reverse order
for i in range(20,10,-1):
    print(i)

# Condition in range:
for i in range(1,21): # 1: Starting Point 21: Ending Point
    if i%5!=0:
        print(i)