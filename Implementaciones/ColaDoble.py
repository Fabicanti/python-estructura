from dataclasses import dataclass
from typing import Any # Any representa "cualquier tipo"

#import pdb; pdb.set_trace()

class Cola_doble():
    @dataclass # decorador para definir una data class
    class _Node:
        _value: Any
        sig: '_Node' 
        prev: '_Node'
    
    __slots__ = ['_len','_start','_end','_back']

    def __init__ (self, iterable = None):
        self._end = self._start = self._back = None
        self._len = 0
        if iterable is not None:
            self.push_end(iterable)


    def push_end(self, value):
        if (self._start == None):
            aux = Cola_doble._Node(value, None, None)
            self._back = aux
            self._start = aux
            self._end = aux
            self._len += 1
        else:
            aux = Cola_doble._Node(value, None, None)
            aux.prev = self._end
            self._end.sig = aux
            
            self._len += 1


    def encolar_frente(self, value):    
        nodoNuevo = Cola_doble._Node(value, None, None)
        #self._head.prev = nodoNuevo
        nodoNuevo.sig = self._head
        self._head = nodoNuevo 
        self._len += 1
        if self._end == None:
            self._end = nodoNuevo

    
    def desencolar_frente(self):
        assert not self.is_empty(), 'La cola esta vacia'
        auxiliar = self._head
        self._head = auxiliar.sig
        #self._head.prev = None
        self._len -= 1
        return auxiliar._value

    def desencolar_final(self):
        assert not self.is_empty(), 'La cola esta vacia'
        auxiliar = self._end
        self._end = auxiliar.prev
        #self._end.sig = None
        self._len -= 1
        return auxiliar._value

    def borrar(self):
        assert not self.is_empty(), 'La cola esta vacia'
        self._end = self._head = None
        self._len = 0

    def __len__(self):
        return self._len

    def __repr__(self):
        values = []
        node = self._head
        while node is not None:
            values.insert(len(values), node._value)
            node = node.sig
        return '(' + ', '.join(repr(x) for x in values) + ')'
        
    def is_empty(self):
        return self._len==0
        
    def __eq__(self, other):
        aux1 = self._start
        aux2 = other._start
        while aux1 == None and aux2 == None:
            if aux1._values == other._values:
                aux1 = aux1.sig
                aux2 = aux2.sig
            else:
                return False
        return True


"""
    @property
    def primero(self):
        assert not self.is_empty(), 'La cola esta vacia'
        #auxiliar = self._head
        return self._head._value
    @property
    def ultimo(self):
        assert not self.is_empty(), 'La cola esta vacia'
        #auxiliar = self._end
        return self._end._value
"""
