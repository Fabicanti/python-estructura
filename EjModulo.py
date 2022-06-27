import time

numero = -1
iteraciones = 1000000

conj = set(range(10000000))
inicio = time.time()

for i in range(iteraciones):
    resultardo = numero in conj

fin = time.time()

print("Con Conjuntos: {:.8f}".format(inicio-fin))

numero = -1
iteraciones = 100

lista = list(range(100))
inicio = time.time()

for i in range(iteraciones):
    resultardo = numero in lista

fin = time.time()

print("Con Listas: {:.8f}".format(inicio-fin))