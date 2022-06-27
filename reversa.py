from Implementaciones.Pila import Pila

def reverse_iterativo(text):
    solucion = ""
    for char in text:
        solucion = char + solucion
    return solucion

def reverse_recursivo(text):
    if len(text) == 1:
        return text
    return reverse_recursivo(text[1:]) + text[:1]

def reverse_pila(text):
    aux = Pila()
    solucion = ""
    for i in text:
        aux.push(i)
    while aux:
        aux2 = aux.pop()
        solucion = solucion + aux2
    return solucion
