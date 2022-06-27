from Implementaciones import nododoble

class DobleCircularList():

    __slots__ = ['_size','_first','_last',]

    def __init__(self):
        self._size = 0
        self._first = self._last = None
    
    @property
    def empty(self):
        return self._size == 0

    @property
    def front(self):
        return self._first._date

    @property
    def back(self):
        return self._last._date

    @property
    def len(self):
        return self._size

    def find(self, find):
        aux = self._first
        count = 1
        while aux._next != self._first:
            if aux._date == find:
                return 'El elemento ', find , 'se encontro en la posicion ', count
            else:
                aux = aux._next
                count += 1
        if aux._date == find:
                return 'El elemento ', find , 'se encontro en la posicion ', count
        return 'Elemento no encontrado'   
    
    def add_front(self, date):
        if self.empty:
            self._first = self._last = nododoble.Nodo(date)
            self._first._next = self._last
            self._first._prev = self._last
            self._last._next = self._first
            self._last._prev = self._first
        else:
            aux = nododoble.Nodo(date)
            aux._next = self._first
            aux._prev = self._last
            self._first._prev = aux
            self._last._next = aux
            self._first = aux
        self._size += 1

    def add_back(self, date):
        if self.empty:
            self._first = self._last = nododoble.Nodo(date)
            self._first._next = self._last
            self._first._prev = self._last
            self._last._next = self._first
            self._last._prev = self._first
        else:
            aux = nododoble.Nodo(date)
            aux._next = self._first
            aux._prev = self._last
            self._first._prev = aux
            self._last._next = aux
            self._last = aux
        self._size += 1

    def remove_front(self):
        if self.empty:
            print("List empty")
        elif self._first == self._last:
            self._first = self._last = None
            self._size -= 1
        else:
            self._first = self._first._next
            self._last._next = self._first
            self._first._prev = self._last
            self._size -= 1
            

    def remove_back(self):
        if self.empty:
            print("List empty")
        elif self._first == self._last:
            self._first = self._last = None
            self._size -= 1
        else:
            self._last = self._last._prev
            self._last._next = self._first
            self._first._prev = self._last
            self._size -= 1
            
    def run_list(self):
        aux = self._first
        while aux:
            print(aux._date)
            aux = aux._next
            if aux == self._first:
                break

