import nododoble

class DoblyList():

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
            self._first = self._last = nododoble.Nodo(date)
        else:
            aux = self._last
            self._last = aux._next = nododoble.Nodo(date)
            self._last._prev = aux
        self._size += 1

    def add_front(self, date):
        if self.is_empty:
            self._first = self._last = nododoble.Nodo(date)
        else:
            aux = nododoble.Nodo(date)
            aux._next = self._first
            self._first._prev = aux
            self._first = aux
        self._size += 1

    def remove_front(self):
        if self.is_empty:
            print("Esta vacia")
        elif self._first._next == None:     
            self._first = self._last = None
            self._size = 0
        else:
            self._first = self._first._next
            self._first._prev = None
            self._size -= 1

    def remove_back(self):
        if self.is_empty:
            print("Esta vacia")
        elif self._first._next == None:
            self._first = self._last = None
            self._size = 0
        else:
            self._last = self._last._prev
            self._last._next = None
            self._size -= 1

    def inverso(self):
        other = self._last
        new = DoblyList()
        while other != None:
            new.add_back(other._date)
            other = other._prev
        return new

    def run_first(self):
        aux = self._first
        while aux != None:
            print(aux._date)
            aux = aux._next

    def run_last(self):
        aux = self._last
        while aux != None:
            print(aux._date)
            aux = aux._prev

    

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
print("*********")
print("back: ", a.back)
print("front:", a.front)
print("*********")
b = DoblyList()
b = a.inverso()
b.run_first()
print("*********")
print("back: ", b.back)
print("front:", b.front)