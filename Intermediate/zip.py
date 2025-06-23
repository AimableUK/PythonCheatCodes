names = ("Navin", "Kiran", "Jeje","Jeje")
comps = ("Dell", "Apple", "samsung","samsung")

zipped = zip(names,comps)
zipped = set(zip(names,comps)) #to converet to the list may to be diplayed you may also use the set or the dictionary

for (a,b) in zipped:
    print(a,b)
    
#2  
lis1 = [23,54,64,2,4,74,6]
tup = ('ukkoo','ahaa','ndababona','yego shaa')
zipped = list(zip(lis1,tup))
print(zipped)
list1, list2 = zip(*zipped)
print(list1,list2)

#3
my_dict = {'a': 1, 'b': 2, 'c': 3}
keys = my_dict.keys()
values = my_dict.values()

zipped = zip(keys,values)

print(list(zipped))

#4
dict1 = {'x': 1, 'y': 2}
dict2 = {'a': 10, 'b': 20}

zipped = zip(dict1.keys(), dict2.keys())
print(list(zipped))

zis  = zip(dict1.values(), dict2.values())
print(list(zis))

#5 Zipping to Combine Dictionaries
keys = {'x': 1, 'y': 2}
values = {'a': 10, 'b': 20}

zipped = dict(zip(keys, values.values()))
print(zipped)
