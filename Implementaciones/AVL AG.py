from dataclasses import dataclass
from typing import Any, Union
##implementacion AVL
                                        ## basicamente iteramos el arbol hasta encontrar el nodo que tiene el valor menor
def _minimum_node(node):                ##la funcion que retorna el minimo nodo
    if node is not None:                ##si el arbol no esta vacio
        while (node.left is not None):  ##mientras el nodo.left no sea un nodo terminal
            node = node.left            ##iteramos
    return node 

                                        ## basicamente iteramos el arbol hasta encontrar el nodo que tiene el mayor valor
def _maximum_node(node):                ##la funcion que retorna el nodo mayor
    if node is not None:                ##si el arbol no esta vacio
        while (node.right is not None): ##mientras el nodo.right no sea un nodo terminal
            node = node.right           ##iteramos
    return node

class Avl():
    @dataclass
    class _Node:
        key: Any                                ##la clave 'se puede comparar'
        value: Any                              ##el valor
        height: int                             ##este representara la altura de cada nodo
        parent: Union['_Node','_Root'] = None   ## el union es porque el padre puede ser o un nodo o la raiz
        left: '_Node' = None                    ##inicializo los nodos
        right: '_Node' = None
    @dataclass
    class _Root:
        left: '_Node' = None                    ##inicializo los nodos
        right: '_Node' = None
        parent: '_Node' = None                  ##el nodo que simboliza el padre, si el padre es None significa que ese nodo es Root
    __slots__ = ['_root','_len']                ##atributos

    def __init__(self, iterable=None):
        self._root = self._Root()
        self._len = 0
        if iterable is not None:
            for key, value in iterable:
                self.insert(key, value)

    def is_empty(self):
        return self._root.left is None   ## aca se usa el nodo izquierdo como nodo base?  es como el prev de la pila que implemente
                                         ##si el nodo izquierdo de la raiz es none, es porque esta vacio

    def __len__(self):
        return self._len                ##devuelve la cantidad de nodos
    
    def begin(self):                    #devuelve la coord que hace referencia al nodo mas chiquito (o mas izqu del arbol)
        return Avl._Coordinate(_minimum_node(self._root))

    def begin_preorden(self):                    #devuelve la coord que hace referencia al nodo mas chiquito (o mas izqu del arbol)
        return Avl._Coordinate(self._root.left)

    def begin_postorden(self):                    #devuelve la coord que hace referencia al nodo mas chiquito (o mas izqu del arbol)
        return Avl._Coordinate(_minimum_node(self._root))

    def end(self):                              #devuelve la coord que hace referencia al ultimo nodo
        return Avl._Coordinate(self._root)      ##devuelve solo root, porque no se pone maximum?----------------------------------------------- 
    
    def minimum(self):
        return Avl._Coordinate(_minimum_node(self._root)) ##retorna una coord que hace referecia al nodo minmo

    def maximum(self):
        return Avl._Coordinate(_maximum_node(self._root.left)) ##retorna una coord que hace referecia al nodo maximo

    def altura(self):
        def do_altura(node):
            if node is None: #si el nodo es None la altura de este es -1 (se sigue explicando debajo del "return 1 + max...")
                return 0
            else: # la altura será la altura máxima entre el subarbol izquierdo y el derecho... + 1 ya que tengo que considerar la altura del propio nodo
                return 1 + max(do_altura(node.left), do_altura(node.right))
                # en el caso de que un nodo tenga None tanto en la hoja hizquierda como en la derecha, al retornar -1, la altura de ese nodo queda igual a cero
        altura = do_altura(self._root.left) #inicio a contar la altura desde la raíz del arbol
        return altura #retorno la altura

                                                ##find recursivo, aporta mas legibilidad al codigo
    def find(self, key):                        ##le paso la clave
        def do_find(node):                      ## funcion interna 
            if (node is None):                  ##si node es none
                return self.end()               ##retorna la coord que hace referencia a root indicando que no lo encontro
            elif (key < node.key):              ##si la clave es mas chica que la clave del nodo actual
                return do_find(node.left)       ##me voy a buscar la clave por el lado izquierdo es decir, lo que busco es mas chiquito que el actual
            elif (key > node.key):              ##si la clave es mas grande que la clave del nodo actual
                return do_find(node.right)      ##me voy a la parte derecha del arbol, es decir, la clave es mas grande que la actual
            else:                               ##hasta que eventualmente key==node.key, por lo tanto
                return Avl._Coordinate(node)    ##retorno la Coord que hace referencia al nodo
        return do_find(self._root.left)         #caso recursivo

    ##con cual nos quedamos?------------------------------------------------------------------------------------------------------------------
    
    ##el find es mejor iterativo que recursivo, porque el recursivo consume mucho mas recursos
    ##ademas te ahorras las pilas de activacion
    
    def find_iterativo(self, key):          #hace lo mismo de la funcion de arriba
        node=self._root.left                #en logica es parecida
        while True:                         #lo que cambia es que hace un bucle
            if (node is None):
                return self.end()
            elif(key < node.key):
                node=node.left
            elif(key > node.key):
                node=node.right
            else: #key == node.key
                return Avl._Coordinate(node)

                                            ##este find lo hice con el proposito de saber si esta o no la clave a buscar
    def find_boolean(self, key):            ##le paso la clave
        def do_find(node):                  ## funcion interna 
            if (node is None):              ##si node es none
                return False                ##retorna False indicando que no lo encontro
            elif (key < node.key):          ##si la clave es mas chica que la clave del nodo actual
                return do_find(node.left)   ##me voy a buscar la clave por el lado izquierdo es decir, lo que busco es mas chiquito que el actual
            elif (key > node.key):          ##si la clave es mas grande que la clave del nodo actual
                return do_find(node.right)  ##me voy a la parte derecha del arbol, es decir, la clave es mas grande que la actual
            else:                           ##hasta que eventualmente key==node.key, por lo tanto
                return True                 ##retorna True indicando que si la encontro
        return do_find(self._root.left)     #caso recursivo

    def len_recursivo(self):
        contador=0
        def do_len(node):
            if(node == None):
                return 0
            return 1 + do_len(node.right) + do_len(node.left)

        contador=do_len(self._root.left)    
        return contador

    ##no es el mismo del erase, pero hace lo mismo (xq el del erase es interno)
    def _assign_parent(self, node, parent):
        if node is not None:                    ##mientras no sea un nodo terminal
            node.parent = parent                ##el padre del nodo es el padre pasado por parametro

    def _update_height(self, node):             ##funcion que actualiza la altura del nodo
        def max(h_left, h_right):   # Retorna la rama mas larga (izq o der)
            if h_left > h_right:
                return h_left
            else:
                return h_right

        left_height = 0
        if node.left is not None:
            left_height = node.left.height
        right_height = 0
        if node.right is not None:
            right_height = node.right.height
        node.height = 1 + max(left_height, right_height)

    def _balance_tree(self, root):

        def rotate_right(root):                     ##root seria el nodo que pasan por parametro
            left_tree = root.left                   ##left_tree es la variable auxiliar que apunta al hijo izq de root
            root.left = left_tree.right             ##ahora pongo al hijo derecho del left de root como hijo iquierdo de root
            self._assign_parent(root.left, root)    ##le asigno el padre 
            left_tree.right = root                  ##ahora el hijo derecho del hijo izquirdo es root, por ende ahora root seria el que fue alguna vez el hijo izq de root
            left_tree.parent = root.parent          ##le asigno el padre
            root.parent = left_tree
            root = left_tree                        ##ahora root es el hijo izquierdo del root original
            self._update_height(root.right)         ##actualizo las alturas
            self._update_height(root)
            return root                             ##retorno root

        def rotate_left(root):                      ##esto hace lo mismo que arriba pero con roles invertidos
            right_tree = root.right                 ##una variable auxiliar que guarda el hijo derecho de root
            root.right = right_tree.left            ##pongo al hijo izquierdo de root como el hijo derecho
            self._assign_parent(root.right, root)   ##le asigno el padre
            right_tree.left = root                  ##ahora el hijo izquierdo de auxiliar es la root original
            right_tree.parent = root.parent         ##ahora el padre de mi root original es el auxiliar
            root.parent = right_tree
            root = right_tree                       ##por ultimo root ahora es auxiliar
            self._update_height(root.left)          ##actualizo las alturas
            self._update_height(root)
            return root

        ##saca la cuanta del FE entre el hijo izquierdo y dercho
        def balance_factor(node): ##FE = height(left) - height(right)
            ## los valores que puede retornar son: -2 -1 0 1 2
            ## si retorna -2 o 2 es porque esta desequilibrado
            factor = 0
            if (node is not None):                  ##si no es una hoja
                if(node.left is not None):          ##si el hijo izquierdo no es teminal
                    factor += node.left.height      ##le sumo a factor su altura
                if(node.right is not None):         ##si el hijo derecho no es terminal
                    factor -= node.right.height     ##le RESTO su altura
            return factor                           ##en caso de que node sea None return 0

        bf = balance_factor(root)                       ##root seria el nodo desequilibrado
        if (bf == 2):                                   ##si el factor de balance es 2 positivo es porque tengo que hacer una rotacion simple derecha
            if (balance_factor(root.left) == -1):       ##pero si el bf es -1 tengo que hacer una rotacion simple a izquierda primero
                root.left = rotate_left(root.left)      ##rotacion a izquierda 
            root = rotate_right(root)                   ##rotacion a derecha
        elif (bf == -2):                                ##si el bf es 2 negativo , debo hacer una rotacion simple a izquierda
            if (balance_factor(root.right) == 1):       ##pero si el bf es +1 tengo que hacer una rotacion simple a derecha
                root.right = rotate_right(root.right)   ##rotacion a derecha
            root = rotate_left(root)                    ##rotacion a izquierda
        else:
            self._update_height(root)                   ##actualizo las alturas
        return root


                                                                ##lo bueno de hacerlo recursivo es porque hace el enganche automatico
                                                                ##a traves de las pilas de activacion
    def insert(self, key, value=None):                          ##funcion que inserta
        def do_insert(node, parent):                            ##funcion interna
            if (node is None):                                  ##
                node = self._Node(key, value, 1,parent)            ##aca se genera el nodo con la clave, el valor y el padre
                coord=Avl._Coordinate(node)                     ## coord es la coord que hace referencia al nodo de arriba
                self._len+=1                                    ##le sumo 1 al len porque el len implementado es de O(1)
            elif(key < node.key):                               ## aca hace lo mismo que en el find pero con la diferencia
                node.left, coord = do_insert(node.left, node)   ## que en vez de pasarle solo el nodo le paso el padre tambien
            elif(key > node.key):
                node.right, coord= do_insert(node.right,node)
            else:  #key == node.key
                node.value = value                              ##le asigno el valor None
                coord = Avl._Coordinate(node)                   ##ya lo explique un par de comentarios arriba
            node=self._balance_tree(node)
            return node, coord                                  ##el return se ejecuta al terminar siempre
            #lo que se logra con esto es hacer el enganche automatico
        ##self._root.left, coord=do_insert(self._root.left, self._root)##primero se ejecuta esto, le paso por parametro el primer nodo y el padre del nodo actual que es la raiz
        self._root.left, coord = do_insert(self._root.left, self._root)
        ## para luego empezar a recorrer el arbol
        return coord ## por ultimo retorno la coord del nodo que acabo de insertar       

    def erase(self, key):
        def do_erase(node):
            if(node is None):                                   ##si en nodo es terminal
                result = False                                  ##significa que no lo encontro, retorna false
                coord = self.end()                              ##retorna la coord que hace referencia a root
            elif(key < node.key):                               ##en los dos elif busco el elemento a borrar
                result, node.left,coord = do_erase(node.left)   ##si la clave es menor a la clave del ndo me voy a izq
            elif(key > node.key):
                result, node.right,coord =do_erase(node.right)  ##si la clave es mayor al la clave del nodo me voy a derecha
            else: #key ==node.key
                result = True                                   ##si lo encontro, devuelve true, indicando que lo borro
                coord = Avl._Coordinate(node).advance()         ##avanzo
                node = erase_node(node)                         ##llamo a la funcion borrar 
            return result,node,coord

            ##existen 3 casos
            ##caso 1 no hay ninguno con la key igual a la que queremos eliminar
            ##caso 2 el nodo a eliminar tiene un subarbol descendiente
            ##caso 3 el nodo a eliminar tiene 2 sub arboles descendientes

        def erase_node(node):                                   ##esta funcion es para buscar la clave
            parent = node.parent
            ##caso1 o caso 2
            if (node.left is None):                             ##si el hijo izq es none
                node=node.right                                 ##me voy por la derecha
            elif (node.right is None):                          ##viceversa de lo de arriba
                node=node.left
            else:                                               ##cuando tanto el nodo izq como der son terminales, tengo que extraer el maximo
                #caso 3 
                node = extract_maximum_from(node)               ##esta funcion se queda con el mayor de la rama izquierda
                                                                ##que sera el que reemplazara el nodo borrado
            assign_parent(node, parent)
            self._len -=1

            return node

        def extract_maximum_from(node):
            prev = None                                         ##me guardo el anterior
            maximum= node.left                                  ##me voy a la izquierda del nodo anterior
                                                                ##y despues me voy todo a la derecha, para buscar el mas grande del sub arbol izquierdo
            while maximum.right is not None:                    #me voy a la derecha
                prev=maximum                                    ##me guardo el padre de max
                maximum=maximum.right                           ##"iteramos" sobre el arbol
            assign_parent(maximum,node.parent)                  ##enganches
            maximum.right=node.right
            assign_parent(maximum.right, maximum)
            if(prev is not None):
                prev.right = maximum.left
                assign_parent(prev.right, prev)
                maximum.left = node.left
                assign_parent(maximum.left, maximum)
            return maximum

        def assign_parent(node, parent):              ##funcion que asigna el padre a un nodo
            if node is not None:                      ##mientras no sea un nodo terminal
                node.parent = parent                  ##el padre del nodo es el padre pasado por parametro

        result, self._root.left, coord=do_erase(self._root.left)
        self._root.left=self._balance_tree(self._root.left)
        ## el result es un bool, dice si  lo encontro o no
        ##el resto es lo mismo que explique arriba
        ##esto se hace para emular el pasaje por referencia ya que python lo hace de forma copia 'de' referencia
        ##yo quiero MODIFICAR el parametro que me pasan
        return result,coord
    
    ##el mejor es iterativo, pero no lo implemente...
    ##lo bueno del copy recursivo es la simpleza del codigo
    def copy(self):                     ##el nombre lo dice todo,en el recursivo te ayudan las pilas de activacion, sino tendriamos que guaradar cada uno
        def do_copy(node, parent):
            if (node is None):          ##si es un nodo terminal
                new_node=None           ## hace el arbol 
            else:
                new_node=Avl._Node(node.key, node.value,node.height,parent) ##aca creo un nuevo nodo del arbol pasandole la clave del nodo, el valor y su padre
                new_node.left = do_copy(node.left,new_node)     ##aca hago un doble llamado recursivo, esto es porque tengo que copiar tanto la rama izq como der
                new_node.right = do_copy(node.right,new_node)
            return new_node
        
                                    ##esto se ejecuta primero
        new_tree=Avl()              ##creo un arbol
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
        __slots__ = ['_node']                       ## atributos de la cordenada

        def __init__(self, node=None):              ##inicializamos la coord
            if isinstance(node,Avl._Coordinate):    ##si es una cordenada la que recibo por parametro en el init
                self._node = node._node             ##obtengo el nodo de esa supuesta coord
            else:
                self._node = node                   ##si solo recibo un nodo, lo asigno directamente

        @property
        def key(self): ##me permite ver la clave
            return self._node.key

        @property
        def value(self): ##me permite ver el valor
            return self._node.value

        @value.setter
        def value(self, value):##redefinir la asignacion del valor
            self._node.value = value##yo puedo modificar el Valor pero NUNCA la clave

        def advance(self):                          ##funcion que sirve para que la coord apunte a otro dato a medida que avanza
            node = self._node
            if node.right is not None:              ##si el nodo que tengo a la derecha no es terminal
                node = _minimum_node(node.right)    ##me voy al mas chico de la rama derecha
            else:                                   ##sino
                while node.parent is not None:      #mientras el padre del nodo no sea none
                    prev = node                     ##aca lo que hago es ir subiendo padre por padre
                    node = node.parent              ##hasta saber de donde vengo
                    if node.right is not prev:      ##si el nodo de donde vengo no es prev, significa que estoy en la izquierda
                        break                       ##corta
            self._node = node
            return self
            ##si vuelvo por la izquierda, debo retornarme a mi y despues siempre hacia la derecha
            ##si vuelvo por la derecha, el padre ya fue procesado, por lo que hay que seguir el "linaje" de padres

        
        def advance_preorden(self): #preorden ya probado ---- si lo vas a probar recorda cambiar begin() que retorne self._root.left
            node = self._node
            prev = node.parent
            if node.left is not None:
                node = node.left
            elif node.right is not None:
                node = node.right
            else:
                while node.parent is not None:
                    prev = node
                    node = node.parent
                    if node.right is not prev and node.right is not None:
                        node = node.right
                        break
            self._node = node
            return self

        def advance_postorden(self):
            def buscar(node):
                while node.right is not None:
                    node = node.right
                    if node.left is not None:
                        node = _minimum_node(node)
                        break
                return node

            node = self._node
            if node.parent is not None:
                prev = node
                node = node.parent
                if node.right is not prev and node.right is not None:
                    node = buscar(node)
            self._node = node
            return self

        def next(self):
            return Avl._Coordinate(self._node).advance()

        def retreat(self):                          #y el retreat hace lo mismo que el advance pero al reves 
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
            return Avl._Coordinate(self._node).retreat()

        def __eq__(self, other):            ##pregunta si dos coordenadas son las mismas 
            return self._node is other._node

        def __repr__(self):
            if hasattr(self._node, 'key'):
                return 'Coordinate({{key: {}, value: {}}})'.format(
                    self._node.key, self._node.value)
            else:
                return 'end()'


    def __eq__(self, other):
        p=self.begin()                                  ##primero creo las variables auxiliares
        q=other.begin()
        while(p!= self.end() and q!=other.end()):       ##mientras los dos no lleguen al final del arbol
            if(p.key != q.key or p.value != q.value):   ##si la clave de uno es diferente del otro o si los valores tambien son diferentes
                return False                            ##retorna falso
            p.advance()                                 ##sino sigo iterando por cada uno
            q.advance()
        return p==self.end() and q==other.end()         ##y al final comparo el final de cada arbol y retorno si son iguales o no

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
        return 'Avl ([' + ', '.join(repr(x) for x in self.items()) + '])'

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

    ##---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
print("---------------------------------------")
print("")
print("INICIALIZANDO BANCO DE PRUEBAS")
print("---------------------------------------")
print("Creo el arbol")
arbol=Avl()
print("---------------------------------------")
print("inserto elementos del 1 al 9 y compruebo que se balanceen")
print("---------------------------------------")
arbol.insert(1,1)
print(arbol)
print("---------------------------------------")
arbol.insert(2,1)
print(arbol)
print("---------------------------------------")
arbol.insert(3,1)
print(arbol)
print("---------------------------------------")
arbol.insert(4,1)
print(arbol)
print("---------------------------------------")
arbol.insert(5,1)
print(arbol)
print("---------------------------------------")
arbol.insert(6,1)
print(arbol)
print("---------------------------------------")
arbol.insert(7,1)
print(arbol)
print("---------------------------------------")
arbol.insert(8,1)
print(arbol)
print("---------------------------------------")
arbol.insert(9,1)
print(arbol)
"""
print("---------------------------------------")
print("pregunto si el arbol esta vacio", arbol.is_empty())
print("---------------------------------------")
print("creo un nuevo arbol")
tree=Avl()
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
#abb=arbol.copy()
#print(abb==tree)
print("---------------------------------------")
print("imprimo arbol")
print(arbol)
print("---------------------------------------")
print("imprimo tree")
print(tree)
print("---------------------------------------")
print("pregunto de nuevo si son iguales")
print(arbol==tree)                
print("---------------------------------------")
print("ahora borro el 4 del tree")
tree.erase(4)
print (tree)
print("---------------------------------------")
print("y por ultimo pregunto si esta el 4 en tree ",tree.find_boolean(4))
print("---------------------------------------")
print("pregunto si esta el 7 en tree ",tree.find_boolean(7))"""
print("el len",len(arbol))
print(arbol.len_recursivo())
"""
tree=Avl()
arbol.insert("p",1)
print(arbol)
print("---------------------------------------")
arbol.insert("u",1)
print(arbol)
print("---------------------------------------")
arbol.insert("j",1)
print(arbol)
print("---------------------------------------")
arbol.insert("a",1)
print(arbol)
print("---------------------------------------")
arbol.insert("s",1)
print(arbol)
print("---------------------------------------")
arbol.insert("b",1)
print(arbol)
print("---------------------------------------")
arbol.insert("g",1)
print(arbol)
print("---------------------------------------")
arbol.insert("f",1)
print(arbol)
print("---------------------------------------")
arbol.insert("z",1)
print(arbol)"""

## inorden: izq ->padre->der
## preorden: padre->izq->der
## postorden: izq->der->padre
## entonces sabes por donde empieza el begin...
## los que tienen izq al principio...llevan el _minimum_node()

a = Avl()
a.insert(1)
print(a)
print(a.altura())
print("---------------------------------------")
a.insert(2)
print(a)
print(a.altura())
print("---------------------------------------")
a.insert(3)
print(a)
print(a.altura())
print("---------------------------------------")
a.insert(4)
print(a)
print(a.altura())
print("---------------------------------------")
a.insert(5)
print(a)
print(a.altura())
print("---------------------------------------")
a.insert(6)
print(a)
print(a.altura())
print("---------------------------------------")
a.insert(7)
print(a)
print(a.altura())
print("---------------------------------------")
a.insert(8)
print(a)
print(a.altura())
print("---------------------------------------")
"""print("imprimendo el arbol en el recorrido inorden")
print(" inorden: izq ->padre->der")
print("---------------------------------------")
coord = a.begin()
for x in range (len(a)):
    print(coord.key)
    coord.advance()
print("---------------------------------------")
print("imprimendo el arbol en el recorrido preorden")
print(a)
print("padre->izq->der")
print("---------------------------------------")
coord = a.begin_preorden()
for x in range (len(a)):
    print(coord.key)
    coord.advance_preorden()
print("---------------------------------------")
print("imprimendo el arbol en el recorrido postorden")
print(a)
print("izq->der->padre")
print("---------------------------------------")
coord = a.begin_postorden()
for x in range (len(a)):
    print(coord.key)
    coord.advance_postorden()
print("---------------------------------------")"""







    

    


       







