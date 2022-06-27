from Implementaciones import nodosimple

class SimpleList():
        
    __slots__ = ['_head', '_size', '_tail']

    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    @property
    def is_empty(self):
        return self._head == None

    @property
    def front(self):
        return self._head._date

    @property
    def back(self):
        return self._tail._date

    def __len__(self):
        return self._size
    
    def len_recursive(self):
        aux = self._head
        def lenR(aux):
            if aux == None:
                return 0
            else:
                aux = aux._next
                return 1 + lenR(aux)
        count = lenR(aux)
        return count


    def add_back(self,date):
        if self.is_empty:
            self._head = self._tail = nodosimple.Nodo(date)
            self._size += 1
        else:
            aux = nodosimple.Nodo(date)
            self._tail._next = aux
            self._tail = aux
            self._size += 1

    def add_front(self,date):
        if self.is_empty:
            self._head = self._tail = nodosimple.Nodo(date)
            self._size += 1
        else:
            aux = nodosimple.Nodo(date)
            aux._next = self._head
            self._head = aux
            self._size += 1
    
    def delete_back(self):
        aux = self._head
        while aux._next != self._tail:
            aux = aux._next
        aux._next = None
        self._tail = aux
        self._size -= 1

    def delete_front(self):
        self._head = self._head._next
        self._size -= 1

    def add_rec(self):
        aux = self._head
        def add(aux):
            if aux == None:
                return 0
            else:
                count = aux._date
                aux = aux._next
                return (count + add(aux))
        count = add(aux)
        return count
    
    def add_iter(self):
        aux = self._head
        count = 0
        while aux != None:
            count = count + aux._date
            aux = aux._next
        return count

    def run_list(self):
        aux = self._head
        while aux != None:
            print(aux._date)
            aux = aux._next


