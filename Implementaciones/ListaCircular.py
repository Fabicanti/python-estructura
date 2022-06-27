from Implementaciones import nodosimple

class CircularList():

    __slots__ = ['_first', '_last', '_size']

    def __init__(self):
        self._first = self._last = None
        self._size = 0

    @property
    def is_empty(self):
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

    def add_back(self, date):
        if self.is_empty:
            self._first = self._last = nodosimple.Nodo(date)
            self._last._next = self._first
        else:
            aux = nodosimple.Nodo(date)
            self._last._next = aux
            aux._next = self._first
            self._last = aux
        self._size += 1

    def add_front(self, date):
        if self.is_empty:
            self._first = self._last = nodosimple.Nodo(date)
            self._last._next = self._first
        else:
            aux = nodosimple.Nodo(date)
            self._last._next = aux
            aux._next = self._first
            self._first = aux
        self._size += 1

    def remove_front(self):
        if self.is_empty:
            print("Is empty")
        elif self._first == self._last:
            self._first = self._last = None
            self._size -= 1
        else:
            self._first = self._first._next
            self._last._next = self._first
            self._size -= 1

    def remove_back(self):
        if self.is_empty:
            print("Is empty")
        elif self._first == self._last:
            self._first = self._last = None
            self._size -= 1
        else:
            aux = self._first
            while aux._next != self._last:
                aux = aux._next
            self._last = aux
            self._last._next = self._first
            self._size -= 1

    def run_list(self):
        aux = self._first
        while aux:
            print(aux._date)
            aux = aux._next
            if aux == self._first:
                break
