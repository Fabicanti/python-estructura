class Pila() :

    # todas las fuciones son de o(1) 
    # escepto la funcion __repr__
    # el metodo length es orden constante tmb pero sin
    # usar el metodo len de python

    __slots__ = ['_values','_count']

    def __init__(self, iterable=None):
        self._values = []
        self._count = 0
        if iterable is not None:
            for value in iterable:
                self.push(value)

    def empty(self):
        return len(self._values) == 0

    @property
    def top(self):
        assert not self.empty(), 'La pila esta vacia'
        return self._values[-1]

    def clear(self):
        self._values.clear()

    def push(self, value):
        self._values.append(value)
        self._count += 1

    def pop(self):
        assert not self.empty(), 'La pila esta vacia'
        self._count -= 1
        return self._values.pop()
        
    def copy(self):
        nueva_pila = Pila()
        nueva_pila._values = self._values.copy()
        return nueva_pila

    def copy_recursivo(self):
        other = Pila()
        aux = Pila(self._values)
        def copy(aux,other):
            if aux.empty():
                return other
            else:
                top = aux.pop()
                copy(aux,other)
                other.push(top)
        copy(aux,other)
        return other

    def length(self):
        return self._count

    def __len__(self):
        return len(self._values)

    def len_recursivo(self):
        aux = Pila(self._values)
        def lenR(aux):
            if aux.empty():
                return 0
            else:
                aux.pop()
                return 1 + lenR(aux)
        count = lenR(aux)
        return count


    def __eq__(self, other):
        return self._values == other._values

    def __repr__(self):
        return 'Pila (['+", ".join(repr(i) for i in self._values) + "])"

