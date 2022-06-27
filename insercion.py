def insercion(list):
    for i in range(1,len(list)):
        elemento = list[i]
        inicio = i-1
        while (inicio >= 0 and list[inicio] > elemento):
            list[inicio + 1] = list[inicio]
            inicio -= 1
        list[inicio + 1] = elemento

list = [5,10,4,2,6,14,55,8]

print("Lista sin ordenar:" + str(list))

insercion(list)

print("Lista ordenada:" + str(list))
