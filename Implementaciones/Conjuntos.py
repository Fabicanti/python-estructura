import nodosimple

class Conjunto():

    __slots__ = ['_first', '_size']

    def __init__(self):
        self._first = None
        self._size = 0

    @property
    def empty(self):
        return self._size == 0

    def __len__(self):
        return self._size

    def add(self, date):
        if self.empty:
            self._first = nodosimple.Nodo(date)
            self._size += 1
        else:
            aux = nodosimple.Nodo(date)
            aux._next = self._first
            self._first = aux
            self._size += 1

    def __eq__(self,other):
        if self._size == other._size:
            aux1 = self._first
            aux2 = other._first
        else:
            return False
        while aux2 is not None:
            while aux1 is not None:
                if aux1._date != aux2._date:
                    aux1 = aux1._next
                elif aux1._date == aux2._date:
                    break
                elif aux1._next == None:
                    return False
            aux2 = aux2._next
            aux1 = self._first            
        return True

    def run_list(self):
        aux = self._first
        while aux != None:
            print(aux._date)
            aux = aux._next



a = Conjunto()
a.add(4)
a.add(1)
a.add(3)
a.add(2)
b = Conjunto()
b.add(1)
b.add(2)
b.add(3)
b.add(4)
print('a')
a.run_list()
print('b')
b.run_list()
print(a==b)