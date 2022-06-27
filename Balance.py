from Implementaciones.Cola import Cola
from Implementaciones.Pila import Pila

def comparacion(Pila,Cola):
    #import pdb; pdb.set_trace()
    balanceo = "Esta Balanceado"
    while (Cola.is_empty()== False and Pila.empty()== False):   
        if (Cola.top == '(' and Pila.top == ')') or (Cola.top == '{' and Pila.top == '}') or (Cola.top == '[' and Pila.top == ']'):
            Cola.pull()
            Pila.pop()
        else:
            balanceo = "No Esta Balanceado"
            break
    return balanceo

def balance(texto):
 #   import pdb; pdb.set_trace()
    assert len(texto)%2 == 0, 'Error secuencia impar.'
    pMitad = Cola()
    sMitad = Pila()

    for i in range(len(texto)):
        if i < (len(texto)//2):
            pMitad.push(texto[i])
        else:
            sMitad.push(texto[i])

    balance = comparacion(sMitad,pMitad)
    return balance


texto = "({[()]})"
texto2 = "[({)}]"

print(balance(texto))
print(balance(texto2))


    
