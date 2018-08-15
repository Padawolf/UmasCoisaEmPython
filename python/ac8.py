def bubbleSort(t):
    n = len(t)
 

    for i in range(n):
 
        for j in range(0, n-i-1):

            if t[j] > t[j+1] :
                t[j], t[j+1] = t[j+1], t[j]
    return t


lista = [2,5,8,41,5,200]
print (bubbleSort(lista))