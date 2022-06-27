class Cola():
    __slots__ = ['_values','_count']
    # todas las fuciones son de o(1) 
    # escepto la funcion __repr__
    # el metodo length es orden constante tmb pero sin
    # usar el metodo len de python

    def __init__(self, iterable = None):
        self._values = []
        self._count = 0
        if iterable is not None:
            self.push(iterable)

    def is_empty(self):
        return len(self._values) == 0

    @property
    def top(self):
        assert not self.is_empty(), 'La cola esta vacia'
        return self._values[-1]

    def clear(self):
        self._values.clear()

    def push(self, value):
        self._values.insert(0,value)
        self._count += 1

    def pull(self):
        assert not self.is_empty(), 'La cola esta vacia'
        return self._values.pop()

    def copy(self):
        nueva_cola = Cola()
        nueva_cola._values = self._values.copy()
        return nueva_cola

    def length(self):
        return self._count

    def __len__(self):
        return len(self._values)

    def __eq__(self, other):
        return self._values == other._values

    def __repr__(self):
        return "Cola{["+", ".join(repr(i) for i in self._values) + "]}"
   