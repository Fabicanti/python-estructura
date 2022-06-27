from Implementaciones.Cola import Cola
from Implementaciones.Pila import Pila

#Entrada de texto
texto = "hola"
texto2 = "somos"

#funcion palindromo
def es_palindromo(texto):
    pila = Pila(texto)
    inverso = ""
    while range(len(pila)):
        inverso += pila.pop()
    return comparacion(inverso,texto)

def comparacion(inverso,texto):   
    if inverso == texto:
        return True
    else :
        return False


print(es_palindromo(texto))
print(es_palindromo(texto2))
