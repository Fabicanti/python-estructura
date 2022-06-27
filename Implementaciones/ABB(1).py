from dataclasses import dataclass
from typing import Any, Union
##implementacion arbol binario de busqueda
## basicamente iteramos el arbol hasta encontrar el nodo que tiene el valor menor
def _minimum_node(node): ##la funcion que retorna el minimo nodo
    if node is not None: ##si el arbol no esta vacio
        while (node.left is not None):  ##mientras el nodo.left no sea un nodo terminal
            node = node.left ##iteramos
    return node 

## basicamente iteramos el arbol hasta encontrar el nodo que tiene el mayor valor
def _maximum_node(node): ##la funcion que retorna el nodo mayor
    if node is not None: ##si el arbol no esta vacio
        while (node.right is not None):  ##mientras el nodo.right no sea un nodo terminal
            node = node.right ##iteramos
    return node

class Abb():
    @dataclass
    class _Node:
        key: Any ##la clave 'se puede comparar'
        value: Any ##el valor
        parent: Union['_Node','_Root'] = None ## el union es porque el padre puede ser o un nodo o la raiz
        left: '_Node' = None ##inicializo los nodos
        right: '_Node' = None
    @dataclass
    class _Root:
        left: '_Node' = None ##inicializo los nodos
        right: '_Node' = None
        parent: '_Node' = None ##el nodo que simboliza el padre, si el padre es None significa que ese nodo es Root
    __slots__ = ['_root','_len'] ##atributos

    def __init__(self, iterable=None):
        self._root = self._Root()
        self._len = 0
        if iterable is not None:
            for key, value in iterable:
                self.insert(key, value)

    def is_empty(self):
        return self._root.left is None ## aca se usa el nodo izquierdo como nodo base?  es como el prev de la pila que implemente
        ##si el nodo izquierdo de la raiz es none, es porque esta vacio

    def __len__(self):
        return self._len ##devuelve la cantidad de nodos

    def len_recursivo(self):
        def do_len(node):
            if(node == None):
                return 0
            return 1 + do_len(node.right) + do_len(node.left)
        return do_len(self._root.left)    
         
    
    def begin(self):#devuelve la coord que hace referencia al nodo mas chiquito (o mas izqu del arbol)
        return Abb._Coordinate(_minimum_node(self._root))

    def end(self):#devuelve la coord que hace referencia al ultimo nodo (siguiente del ultimo)
        return Abb._Coordinate(self._root)##devuelve solo root, porque no se pone maximum?----------------------------------------------- 
    
    def minimum(self):
        return Abb._Coordinate(_minimum_node(self._root)) ##retorna una coord que hace referecia al nodo minmo

    def maximum(self):
        return Abb._Coordinate(_maximum_node(self._root.left)) ##retorna una coord que hace referecia al nodo maximo

    ##find recursivo, aporta mas legibilidad al codigo
    def find(self, key): ##le paso la clave
        def do_find(node): ## funcion interna 
            if (node is None): ##si node es none
                return self.end() ##retorna la coord que hace referencia a root indicando que no lo encontro
            elif (key < node.key): ##si la clave es mas chica que la clave del nodo actual
                return do_find(node.left) ##me voy a buscar la clave por el lado izquierdo es decir, lo que busco es mas chiquito que el actual
            elif (key > node.key): ##si la clave es mas grande que la clave del nodo actual
                return do_find(node.right)##me voy a la parte derecha del arbol, es decir, la clave es mas grande que la actual
            else: ##hasta que eventualmente key==node.key, por lo tanto
                return Abb._Coordinate(node) ##retorno la Coord que hace referencia al nodo
        return do_find(self._root.left) #caso recursivo

    ##cuales son las desventajas y ventajas de ambos ------------------------------------------------------------------------------------------------------------------
    
    ##el find es mejor iterativo que recursivo, porque el recursivo consume mucho mas recursos
    ##ademas te ahorras las pilas de activacion
    
    def find_iterativo(self, key):#hace lo mismo de la funcion de arriba
        node=self._root.left#en logica es parecida
        while True:#lo que cambia es que hace un bucle
            if (node is None):
                return self.end()
            elif(key < node.key):
                node=node.left
            elif(key > node.key):
                node=node.right
            else: #key == node.key
                return Abb._Coordinate(node)

    ##este find lo hice con el proposito de saber si esta o no la clave a buscar
    def find_boolean(self, key): ##le paso la clave
        def do_find(node): ## funcion interna 
            if (node is None): ##si node es none
                return False ##retorna False indicando que no lo encontro
            elif (key < node.key): ##si la clave es mas chica que la clave del nodo actual
                return do_find(node.left) ##me voy a buscar la clave por el lado izquierdo es decir, lo que busco es mas chiquito que el actual
            elif (key > node.key): ##si la clave es mas grande que la clave del nodo actual
                return do_find(node.right)##me voy a la parte derecha del arbol, es decir, la clave es mas grande que la actual
            else: ##hasta que eventualmente key==node.key, por lo tanto
                return True ##retorna True indicando que si la encontro
        return do_find(self._root.left) #caso recursivo 

    ##lo bueno de hacerlo recursivo es porque hace el enganche automatico
    ##a traves de las pilas de activacion
    def insert(self, key, value=None): ##funcion que inserta
        def do_insert(node, parent): ##funcion interna
            if (node is None): ##
                node = Abb._Node(key, value, parent)##aca se genera el nodo con la clave, el valor y el padre
                coord=Abb._Coordinate(node)## coord es la coord que hace referencia al nodo de arriba
                self._len+=1 ##le sumo 1 al len porque el len implementado es de O(1)
            elif(key < node.key):## aca hace lo mismo que en el find pero con la diferencia
                node.left, coord = do_insert(node.left, node)## que en vez de pasarle solo el nodo le paso el padre tambien
            elif(key > node.key):
                node.right, coord= do_insert(node.right,node)
            else:  #key == node.key
                node.value = value ##le asigno el valor None
                coord = Abb._Coordinate(node) ##ya lo explique un par de comentarios arriba
            return node, coord ##el return se ejecuta al terminar siempre
            #lo que se logra con esto es hacer el enganche automatico
        self._root.left, coord=do_insert(self._root.left, self._root)##primero se ejecuta esto, le paso por parametro el primer nodo y el padre del nodo actual que es la raiz
        ## para luego empezar a recorrer el arbol
        return coord ## por ultimo retorno la coord del nodo que acabo de insertar  

    def insert_iterativo(self, key, value=None):##-----------------------------------------------------------------------------------------------------------------------------
        node=self._root.left                           #creo una variable auxiliar que tendra primer nodo del arbol, el hijo izquierdo de la raiz.
        parent=self._root                              #creo una variable auxiliar padre para poder ir guardando el padre durante el recorrido del arbol para poder luego asignarselo al nuevo nodo insertado
        while node is not None:                        #recorro el arbol siempre que el nodo en la ubicacion del recorrido no sea None
            if key<node.key:                           #si la clave (key) del nodo que se quiere insertar es menor a la del nodo en la ubicacion del recorrido del arbol
                parent=node                            #entonces el padre del nodo a insertar pasara a ser el nodo en la ubicacion del recorrido que se esta comparando
                node=node.left                         #le reasigno el valor al nodo auxiliar para mi recorrido asignandole el valor de su hijo a la izquierda, de esta manera, voy bajando hacia la izquierda en el arbol
            elif key>node.key:                         #si la clave del nodo que se quiere insertar es mayor que la del nodo en la ubicacion del recorrido en el arbol
                parent=node                            #entonces el padre del nodo a instertar pasara a ser el nodo en la ubicacion del recorrido que se esta comparando
                node=node.right                        #le reasigno el valor al nodo auxiliar para mi recorrido asignandole el valor de su hijo a la derecha, de esta manera, voy bajando hacia la derecha en el arbol
            else:                                      #si la clave no es menor ni mayor, entonces sera igual, por lo tanto el nodo que se quiere insertar ya existe en el arbol
                node.value=value                       #cambio el valor interno que tiene el nodo en el arbol por le valor del nodo que se quiere insertar
                return Abb._Coordinate(node)            #retorno una coordenada con el nodo que se inserto, que en realidad, en este caso, solo se cambio su valor interno 
        node=self._Node(key,value,parent)              #si el nodo en el recorrido es none, entonces se saldra del while,por lo tanto debere insertar el nodo en ese lugar, por lo tanto creo mi nuevo nodo con su clave, su valor y su padre que sera el anterior a el mismo
        if key>parent.key:                             #si la clave del nodo a insertar es mayor que la del padre
            parent.right=node                          #entonces insertare el nuevo nodo a la derecha del padre,ya que es mayor a el
        else:                                          #en cambio, si la clave del nodo a insertar es menor que la del padre
            parent.left=node                           #entonces insertare el nuevo nodo a la izquierda del padre, ya que es menor a el
        coord=Abb._Coordinate(node)                     #creo una nueva coordenada con el nuevo nodo insertado
        self._len+=1                                   #aumento en uno la cantidad de nodos que tiene el arbol
        return coord                                   #retorno la coordenada

    def insertar_iterativo(self, key, value=None):
        node=self._root.left                          
        parent=None                         
        while node is not None:                        
            if key<node.key:                           
                parent=node                            
                node=node.left                        
            elif key>node.key:                         
                parent=node                            
                node=node.right                        
            else:                                      
                return False                                 
        neWnode=self._Node(key,value,parent)              
        if key>parent.key:                             
            parent.right=neWnode                          
        else:                                          
            parent.left=neWnode    
        return True    
       

    def erase(self, key):
        def do_erase(node):
            if(node is None): ##si en nodo es terminal
                result = False ##significa que no lo encontro, retorna false
                coord = self.end() ##retorna la coord que hace referencia a root
            elif(key < node.key):##en los dos elif busco el elemento a borrar
                result, node.left,coord = do_erase(node.left)##si la clave es menor a la clave del ndo me voy a izq
            elif(key > node.key):
                result, node.right,coord =do_erase(node.right)##si la clave es mayor al la clave del nodo me voy a der
            else: #key ==node.key
                result = True ##si lo encontro, devuelve true, indicando que lo borro
                coord = Abb._Coordinate(node).advance()         ##avanzo por la parte ver -------------------------------------------------------------------------------------------------------------------
                node = erase_node(node)##llamo a la funcion borrar 
            return result,node,coord

            ##caso 1 no hay ninguno con la key igual a la que queremos eliminar
            ##caso 2 el nodo a eliminar tiene un subarbol descendiente
            ##caso 3 el nodo a eliminar tiene 2 sub arboles descendientes

        def erase_node(node):##esta funcion es para buscar la clave
            parent = node.parent
            ##caso1 o caso 2
            if (node.left is None): ##si el hijo izq es none
                node=node.right ##me voy por la derecha
            elif (node.right is None):##viseversa de lo de arriba
                node=node.left
            else:##cuando tanto el nodo izq como der son terminales, tengo qur extraer
                #caso 3 
                node = extract_maximum_from(node) ##esta funcion se queda con el mayor de la rama izquierda
                ##que sera el que reemplazara el nodo borrado
            assign_parent(node, parent)
            self._len -=1

            return node

        def extract_maximum_from(node):##-------------------------------------------------------------------------------------no entiendo que hace
            prev = None ##me guardo el anterior
            maximum= node.left ##me voy a la izquierda del nodo anterior
            ##y despues me voy todo a la derecha, para buscar el mas grande del sub arbol izquierdo
            while maximum.right is not None: #me voy a la derecha
                prev=maximum ##me guardo el padre de max
                maximum=maximum.right ##"iteramos" sobre el arbol
            assign_parent(maximum,node.parent) ##enganches
            maximum.right=node.right
            assign_parent(maximum.right, maximum)
            if(prev is not None):
                prev.right = maximum.left
                assign_parent(prev.right, prev)
                maximum.left = node.left
                assign_parent(maximum.left, maximum)
            return maximum


        def assign_parent(node, parent):##funcion que asigna el padre a un nodo
            if node is not None: ##mientras no sea un nodo terminal
                node.parent = parent ##el padre del nodo es el padre pasado por parametro


        result, self._root.left, coord=do_erase(self._root.left)
        ## el result es un bool, dice si  lo encontro o no
        ##el resto es lo mismo que explique arriba
        ##esto se hace para emular el pasaje por referencia ya que python lo hace de forma copia 'de' referencia
        ##yo quiero MODIFICAR el parametro que me pasan
        return result,coord
    
    def copy(self):##el nombre lo dice todo, es mejor siendo recursivo, porque te ayudan las pilas de activacion, sino tendriamos que guaradar
        def do_copy(node, parent):
            if (node is None):##si es un nodo terminal
                new_node=None ## hace el arbol 
            else:
                new_node=Abb._Node(node.key, node.value,parent) ##aca creo un nuevo nodo del arbol pasandole la clave del nodo, el valor y su padre
                new_node.left = do_copy(node.left,new_node)##aca hago un doble llamado recursivo, esto es porque tengo que copiar tanto la rama izq como der
                new_node.right = do_copy(node.right,new_node)
            return new_node
        
        ##esto se ejecuta primero
        new_tree=Abb()##creo un arbol
        new_tree._root.left= do_copy(self._root.left, new_tree._root)
        ##el nodo siguiente de root de newTree es do_copy(le paso el nodo siguiente de root de mi arbol que quiero copiar, la raiz del arbol que quiero copiar)
        new_tree._len = self._len ##copio el len
        return new_tree##retorno el nuevo arbol

    def clear(self):
        self._root.left = None
        self._len = 0


    #estas dos estan de mas, no es necesario en el parcial
    ##se usa: if (CLAVE in DICCIONARIO)
        ##con diccionario siendo el nombre del arbol
    def __contains__(self,key):##retorna si contiene la clave o no
        return self.find(key) != self.end()

    ##se usa: arbol[clave]
    def __getitem__(self,key):
        p=self.find(key)
        if (p == self.end()):
            raise KeyError(key)
        return p.value

    
    ##CLASE COORDENADA----------------------------------------------------------------------------------------------------------------
    class _Coordinate():
        __slots__ = ['_node']## atributos de la cordenada

        def __init__(self, node=None):  ##inicializamos la coord
            if isinstance(node,Abb._Coordinate):##si es una cordenada la que recibo por parametro en el init
                self._node = node._node ##obtengo el nodo de esa supuesta coord
            else:
                self._node = node ##si solo recibo un nodo, lo asigno directamente

        @property
        def key(self): ##me permite ver la clave
            return self._node.key

        @property
        def value(self): ##me permite ver el valor
            return self._node.value

        @value.setter
        def value(self, value):##redefinir la asignacion del valor
            self._node.value = value##yo puedo modificar el Valor pero NUNCA la clave

        def advance(self): ##funcion que sirve para que la coord apunte a otro dato a medida que avanza
            node = self._node
            if node.right is not None: ##si el nodo que tengo a la derecha no es terminal
                node = _minimum_node(node.right) ##me voy al mas chico de la rama derecha
            else:                                ##sino
                while node.parent is not None: #mientras el padre del nodo no sea none
                    prev = node ##aca lo que hago es ir subiendo padre por padre
                    node = node.parent ##hasta saber de donde vengo
                    if node.right is not prev: ##si el nodo de donde vengo no es prev, significa que estoy en la izquierda
                        break ##corta
            self._node = node
            return self
            ##si vuelvo por la izquierda, debo retornarme a mi y despues siempre hacia la derecha
            ##si vuelvo por la derecha, el padre ya fue procesado, por lo que hay que seguir el "linaje" de padres


        def next(self):
            return Abb._Coordinate(self._node).advance()

        def retreat(self): #y el retreat hace lo mismo que el advance pero al reves 
            node = self._node
            if node.left is not None:
                node = _maximum_node(node.left)
            else:
                while node.parent is not None:
                    prev = node
                    node = node.parent
                    if node.left is not prev:
                        break
            self._node = node
            return self
           
        def prev(self):
            return Abb._Coordinate(self._node).retreat()

        def __eq__(self, other):##pregunta si dos coordenadas son las mismas 
            return self._node is other._node

        def __repr__(self):
            if hasattr(self._node, 'key'):
                return 'Coordinate({{key: {}, value: {}}})'.format(
                    self._node.key, self._node.value)
            else:
                return 'end()'


    def __eq__(self, other):
        p=self.begin()##primero creo las variables auxiliares
        q=other.begin()
        while(p!= self.end() and q!=other.end()): ##mientras los dos no lleguen al final del arbol
            if(p.key != q.key or p.value != q.value):##si la clave de uno es diferente del otro o si los valores tambien son diferentes
                return False##retorna falso
            p.advance()##sino sigo iterando por cada uno
            q.advance()
        return p==self.end() and q==other.end()##y al final comparo el final de cada arbol y retorno si son iguales o no

    def eq_recursivo(self, other):
        def do_eq(p , q):
            if(p is None or q is None):
                if(p is None and q is None):
                    return True
                else:
                    return False
            if(p.key != q.key or p.value != q.value):
                return False
            if p.right is not None and q.right is not None:
                do_eq(p.right,q.right)
            if p.left is not None and q.left is not None:
                do_eq(p.left,q.left)
        return do_eq(self._root.left,other._root.left)
            
            


    ##implementar otra forma para practicar
    #@ver esto !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    def advance(self): ##funcion que sirve para que la coord apunte a otro dato a medida que avanza
            node = self._node
            if node.right is not None: ##si el nodo que tengo a la derecha no es terminal
                node = _minimum_node(node.right) ##me voy al mas chico de la rama derecha
            else:                                ##sino
                while node.parent is not None: #mientras el padre del nodo no sea none
                    prev = node ##aca lo que hago es ir subiendo padre por padre
                    node = node.parent ##hasta saber de donde vengo
                    if node.right is not prev: ##si el nodo de donde vengo no es prev, significa que estoy en la izquierda
                        break ##corta
            self._node = node
            return self
            ##si vuelvo por la izquierda, debo retornarme a mi y despues siempre hacia la derecha
            ##si vuelvo por la derecha, el padre ya fue procesado, por lo que hay que seguir el "linaje" de padres


    ##para que el arbol sea iterable-------------------------------------------------------------------------------------
    def items(self):
        pos = self.begin()
        end = self.end()
        while pos != end:
            yield pos.key, pos.value
            pos.advance()


    def keys(self):
        for key, _ in self.items():
            yield key


    def values(self):
        for _, value in self.items():
            yield value


    def __iter__(self):
        return self.keys()

    #--------------------------------------------------------------------------------------------------------------------


    def __repr__(self):
        return 'Abb ([' + ', '.join(repr(x) for x in self.items()) + '])'

    def __str__(self):
        #Funcion que imprime el arbol como se debe
        def calculate_placement(node, level):
            if node is None:
                return 0
                
            nonlocal count
            m1 = calculate_placement(node.left, level + 1)
            placements.append((level, count, node))
            count += 1
            m3 = calculate_placement(node.right, level + 1)
            return max(m1, len(str(node.key)), m3)

        count = 0
        placements = []
        key_len = calculate_placement(self._root.left, 0) + 2

        lines = []
        prev_level = -1
        for level, pos, node in placements:
            i = 2 * level
            while len(lines) <= i:
                lines.append('')

            skip = ' ' * (pos * key_len - len(lines[i]))
            lines[i] += skip + '[{:^{}}]'.format(node.key, key_len - 2)

            if prev_level != -1:
                if prev_level < level:
                    i = 2 * prev_level + 1
                    skip = ' ' * (pos * key_len - len(lines[i]))
                    c = '\\'
                else:
                    i = 2 * level + 1
                    skip = ' ' * (pos * key_len - len(lines[i]) - 1)
                    c = '/'

                lines[i] += skip + '{:>{}}'.format(c,  key_len // 2)

            prev_level = level

        return '\n'.join(lines)

print("---------------------------------------")
print("")
print("INICIALIZANDO BANCO DE PRUEBAS")
print("---------------------------------------")
print("Creo el arbol")
arbol=Abb()
print("---------------------------------------")
print("inserto elementos del 1 al 9 y compruebo que se balanceen")
print("---------------------------------------")
arbol.insert(4,1)
print(arbol)
print("---------------------------------------")
arbol.insert(2,1)
print(arbol)
print("---------------------------------------")
arbol.insert(3,1)
print(arbol)
print("---------------------------------------")
arbol.insert(9,1)
print(arbol)
print("---------------------------------------")
arbol.insert(30,1)
print(arbol)
print("---------------------------------------")
arbol.insert(0,1)
print(arbol)
print("---------------------------------------")
arbol.insert(5,1)
print(arbol)
print("---------------------------------------")
arbol.insert(8,1)
print(arbol)
print("---------------------------------------")
arbol.insert(9,1)
print(arbol)
print("---------------------------------------")
print("pregunto si el arbol esta vacio", arbol.is_empty())
print("---------------------------------------")
print("creo un nuevo arbol")
tree=Abb()
print(tree)
print("pregunto si el arbol esta vacio", tree.is_empty())
print("---------------------------------------")
print("le agrego un nodo a el tree")
tree.insert(2,1)
print(tree)
print("---------------------------------------")
print("pregunto si son iguales")
print(tree==arbol)
print("---------------------------------------")
print("ahora limpio el tree")
tree.clear()
print("---------------------------------------")
print("ahora copio el arbol en tree")
tree=arbol.copy()
print("---------------------------------------")
print("imprimo arbol")
print(arbol)
print("---------------------------------------")
print("imprimo tree")
print(tree)
print("---------------------------------------")
print("pregunto de nuevo si son iguales")
print(tree==arbol)##-------------------------------------------------------------------------------------------
print("---------------------------------------")
print("")
print("---------------------------------------")
print("ahora borro el 4 del tree") ##--------------------------------------------------------------------------
tree.erase(4)
print (tree)
print("---------------------------------------")
print("y por ultimo pregunto si esta el 4 ",tree.find_boolean(4))
print("---------------------------------------")
print("pregunto si esta el 30 ",tree.find_boolean(30))
print(tree.insertar_iterativo(90))
print(tree)
print(tree.len_recursivo())

abelardo=Abb()
abelardo.insert(1,1)
abelardo.insert(3,1)
abelardo.insert(5,1)
abelardo.insert(6,1)
abelardo.insert(7,1)
print(abelardo)
print("---------------------------------------")
belardo=Abb()
#"""
belardo.insert(1,1)
belardo.insert(3,1)
belardo.insert(5,1)
belardo.insert(6,1)
belardo.insert(7,1)
"""
belardo.insert(2,1)
belardo.insert(2,1)
belardo.insert(3,1)
belardo.insert(4,1)
belardo.insert(5,1)
"""
print(belardo)
print("---------------------------------------")
print(abelardo.eq_recursivo(belardo))

    

    


       







