def ordenar(list):
    for i in range(len(list)):
        min = i
        for j in range(i+1, len(list)):
            if list[j] < list[min]:
                min = j
        list[i], list[min] = list[min], list[i]


list = [5,10,4,2,6,14,55,8]

print("Lista sin ordenar:" + str(list))

ordenar(list)

print("Lista ordenada:" + str(list))
