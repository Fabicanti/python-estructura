from Implementaciones.Cola import Cola
from Implementaciones.Pila import Pila

#Entrada de numeros a la pila
numeros = Pila()
numeros.push(0)
numeros.push(1)
numeros.push(2)
numeros.push(3)
numeros.push(4)
numeros.push(5)
numeros.push(6)
numeros.push(7)
numeros.push(8)
numeros.push(9)
print(numeros)

#funcion para invertir numeros de una pila
def inverso(numeros):
    invertido = Pila()
    while range(len(numeros)):
        invertido.push(numeros.pop())
    return invertido
print(inverso(numeros))
