pos =-1
def search(lista,n):

	i = 0
	while i<len(lista): #same as this :	for i,element in enumerate(lista):

		if lista[i] == n:
			globals()['pos'] = i
			print(f'found at index {i+1}')
			return True
		i = i+1


lista = [35,89,4,6,6,12,43]

n = int(input("enter a search number"))
if search(lista,n):
	print('Again found at ',pos+1)
else:
	print('not found')



#2 way
def search(lista, n):
    indices = [i for i, element in enumerate(lista) if element == n]
    if indices:
        print(f'found at indices {indices}')
        return True
    return False #this may not be put

lista = [35, 89, 4, 6, 6, 12, 43]
n = int(input("eneter a search number: "))
if search(lista, n):
    print('found')
else:
    print('not found')

