

lista = [1,2,3,4,5]
for x in range (1, len(lista)+1):
    lista[x] = lista[len(lista)-x]
print (lista)



