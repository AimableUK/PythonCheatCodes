

lis1 = [23,54,64,2,4,74,6]
tup = ('ukkoo','ahaa','ndababona','yego shaa')
zipped = list(zip(lis1,tup))
print(zipped)
list1, list2 = zip(*zipped)
print(list1,list2)