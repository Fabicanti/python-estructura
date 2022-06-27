def lineal (list, buscado):
    i = 0
    while (i <= len(list)-1):
        if (list[i] == buscado):
            return print("El elemento buscado se encuentra en la posicion:" , i)
        else:
            i+=1
    else:
        return -1

list = [0,1,2,3,4,5,6,7,8,9,10,11]
buscado = 5
lineal(list,buscado)