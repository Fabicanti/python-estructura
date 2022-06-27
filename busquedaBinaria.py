def binaria(list, buscado):
    inicio = 0
    fin = len(list)-1
    while inicio <= fin:
        mid = (inicio + fin) // 2 
        if list[mid] == buscado:
            return print("El elemento buscado se encuentra en la posicion:" , mid)
        else:
            if list[mid] > buscado:
                fin = mid - 1
                print("Buscando:",list[:mid])
            else: 
                inicio = mid + 1
                print("Buscando:",list[mid:])
    return print("El elemento buscado se encuentra en la posicion:" , mid)

list = [0,1,2,3,4,5,6,6,7,8,9]
buscado = 8
binaria(list,buscado)