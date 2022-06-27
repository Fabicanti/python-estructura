from Implementaciones.Pila import Pila
""" 
p = Pila("Hola")
p.push("chau",)
p.push(5)
print(p.length())
print(p)
print(p.pop())
print(p)
print(p.top)
p.pop()
print(p)
p.pop()
print(p.empty())
print("**********")
a = p.copy_recursivo()
print("copy recursivo")
print("original", p)
print("copia", a)
print("**********")
print("len recursivo")
print("recursivo", a.len_recursivo())
print("original", a.length())
 """
from Implementaciones.Cola import Cola

"""
c = Cola('hola')
c.push("chau")
c.push(5)
print(c)
print(c.pull())
print(c)
print(c.top)
c.pull()
print(c)
c.pull()
print(c.is_empty()) """

from Implementaciones.Fecha import Fecha

""" f = Fecha()
f.setFecha(28021990)
print(f)
f2 = Fecha(28021990)
print(f2)
if (f == f2) :
    print(True)
else:
    print(False)
f.setaño(2005)
f.setMes(10)
f.setDia(22)
print(f)
f.eliminar()
print(f)
""" 

from Implementaciones.ColaDoble import Cola_doble

"""
a = Cola_doble()
print(len(a))
print(a.is_empty())
a.encolar_frente(10)
a.encolar_frente(15)
a.encolar_final(17)
a.encolar_final(25)
print(a)
print("ultimo: ", a.ultimo)
print("primero: ", a.primero)
print(len(a))
print(a.is_empty())
print("desencolando: ", a.desencolar_frente())
print("desencolando: ", a.desencolar_final())
print(a)
a.borrar()
print(a)
"""

from Implementaciones.ListaSimpleNodo import SinglyLinkedList

""" a = SinglyLinkedList()
a.insert_front(1)
a.insert_front(2)
a.insert_front(3)
a.insert_front(4)
a.insert_front(5)
print(a)
print(a.is_empty())
print(len(a))
a.insert_after(2,4)
print(a) """

from Implementaciones.ListaSimple import SimpleList

""" 
a = SimpleList()
a.add_back(1)
a.add_back(2)
a.add_back(3)
a.add_back(4)
a.run_list()
print("*******************")
print(a.front)
print("*******************")
print("suma recursiva", a.add_rec())
print("suma iterativa", a.add_iter())
print("*******************")
a.add_front(1)
a.add_front(2)
a.add_front(3)
a.add_front(4)
a.run_list()
print(a.back)
print("*******************")
a.delete_back()
a.run_list()
print("*******************")
a.delete_front()
a.run_list()
print("*******************")
print("original", a._size)
print("recursivo", a.len_recursive())
 """

from Implementaciones.ListaDoble import DoblyList

a = DoblyList()
a.add_back(4)
a.add_back(3)
a.add_back(2)
a.add_back(1)
print("back: ", a.back)
a.run_last()
print("***************")
a.add_front(5)
a.add_front(6)
print("front: ", a.front)
a.run_first()
print("*********")
print("back: ", a.back)
a.remove_back()
print("front: ", a.front)
a.remove_front()
a.run_first() 




from Implementaciones.ListaDobleNodo import DoblyList

"""
a = DoblyList()
a.add_front(1)
a.add_front(10)
a.add_front(100)
a.add_front(1000)
a.add_end(1000)
a.add_end(100)
a.add_end(10)
a.add_end(1)
print(a)
"""

from factorial import factorial_iterativo, factorial_recursivo

""" print("recursivo")
print("factorial de 0:", factorial_recursivo(0))
print("factorial de 1:", factorial_recursivo(1))
print("factorial de 5:", factorial_recursivo(5))
print("*******************************")
print("iterativo")
print("factorial de 0:", factorial_iterativo(0))
print("factorial de 1:", factorial_iterativo(1))
print("factorial de 5:", factorial_iterativo(5))
 """

from reversa import reverse_iterativo, reverse_recursivo

""" text = "hola"
text2 = "chau"
text3 = "estar"
print("************************")
print("iterativo:")
print(reverse_iterativo(text))
print("************************")
print("recursivo:")
print(reverse_recursivo(text2))
print("************************")
print("pila:")
print(reverse_pila(text3))
 """

from Implementaciones.ListaCircular import CircularList

""" 
a = CircularList()
a.remove_back()
a.add_front(2)
a.add_front(3)
a.add_back(20)
a.add_back(30)
print("***************")
print("lista circular.")
print("front ", a.front)
print("back ", a.back)
print("***************")
a.run_list()
print("remove front")
print("***************")
a.remove_front()
print("front ", a.front)
print("back ", a.back)
print("***************")
a.run_list()
print("remove back")
print("***************")
a.remove_back()
print("front ", a.front)
print("back ", a.back)
print("***************")
a.run_list()
 """

from Implementaciones.ListaCircularDoble import DobleCircularList

"""
a = DobleCircularList()
print("empty", a.empty)
a.add_back(4)
a.add_back(5)
a.add_back(6)
a.add_front(1)
a.add_front(2)
a.add_front(3)
print("front", a.front)
print("back", a.back)
print("empty", a.empty)
print("len ", a.len)
print("***************")
a.run_list()
print("***************")
print("remove")
print("back", a.back)
print("front", a.front)
a.remove_back()
a.remove_front()
print("***************")
a.run_list()
print("***************")
print("front", a.front)
print("back", a.back)
print("empty", a.empty)
print("len ", a.len)
print("***************")
print(a.find(5))
"""

