from dataclasses import dataclass
from tkinter.messagebox import RETRY
from typing import Any



class SinglyLinkedList():

    @dataclass
    class _Head:
        next: '_Node' = None
    
    @dataclass
    class _Node:
        value: Any
        next: '_Node' = None

    __slots__ = ['_head','_size']
    
    def __init__(self, value = None):
        if value == None:
            self._head = SinglyLinkedList._Head(None)
            self._size = 0
        else:
            new = SinglyLinkedList._Node(value, None)
            self._head = SinglyLinkedList._Head(new)
            self._size += 1    
        
    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0
    
    def clean(self):
        self._head.next = None
        
    def __iter__(self):
        # Usando abstracciones
        p = self.begin()
        while p != self.end():
            yield p.value
            p.advance()

        # Otra opción más "a mano"...
        # nodo = self._head.next
        # while nodo is not None:
        #     yield nodo.value
        #     nodo = nodo.next

    def begin(self):
        return SinglyLinkedList.Coordinate(self._head.next)


    def end(self):
        return SinglyLinkedList.Coordinate(None)


    def before_begin(self):
        return SinglyLinkedList.Coordinate(self._head)

    def insert_after(self, coord, value):
        current = coord._node
        new_node = SinglyLinkedList._Node(value=value, next=current.next)
        current.next = new_node
        self._size += 1
        return SinglyLinkedList.Coordinate(new_node)

    def insert_front(self, value):
        self.insert_after(self.before_begin(), value)

    def erase_after(self, coord):
        current = coord._node
        current.next = current.next.next
        self._size -= 1
        return coord.next()

    
    def __repr__(self):
        return 'SinglyLinkedList([' + ', '.join(repr(v) for v in self) + '])'

    """
    def __repr__(self):
        values = []
        aux = self._head.next
        while aux is not None:
            values.insert(len(values), aux.value)
            aux = aux.next
        return '\n'.join(repr(x) for x in values)
    """    

    class Coordinate():
        __slots__ = ['_node']

        def __init__ (self, coordinate_or_node):
            if isinstance(coordinate_or_node,SinglyLinkedList.Coordinate):
                self._node = coordinate_or_node._node
            else:
                self._node = coordinate_or_node
            
        @property
        def value(self):
            return self._node.value

        @value.setter
        def value(self,value):
            self._node.value = value

        
        def advance (self):
            self._node = self._node.next
            return self

        def next (self):
            c = SinglyLinkedList.Coordinate(self._node)
            return c.advance()

        def __eq__ (self, other):
            return self._node is other._node    
  

