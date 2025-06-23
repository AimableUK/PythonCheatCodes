def my_fun(*iterr): #this collects as many as provided args
    print(iterr)
    
my_fun(43,52,6,3456,5,252,5236,754)




#2
t = (3,5)
divmod(*t) #this unpacks a list, sequence ,turple and (it will unpack t and pass it as two args)
print(divmod)