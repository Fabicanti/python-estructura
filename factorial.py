def factorial_recursivo(numero):
    if numero == 0:
        return 1
    else:
        return numero * factorial_recursivo(numero - 1)

def factorial_iterativo(numero):
    if numero == 0:
        return 1
    num = 1
    while numero >= 1:
        num = num * numero
        numero = numero - 1
    return num
