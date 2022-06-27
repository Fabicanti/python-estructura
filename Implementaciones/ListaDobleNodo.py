from nododoble import Head, Nodo, Coordinate, Iterator

class DoblyList():

    __slots__ = ['_head', '_size']

    def __init__ (self):
        self._head = Head()
        self._head._prev = self._head._next = self._head
        self._size = 0

    @property       
    def is_empty(self):
        return self._head._next is self._head
    
    @property
    def front(self):
        assert not self.is_empty, 'Empty list'
        return self._head._next._date

    @property
    def back(self):
        assert not self.is_empty, 'Empty list'
        return self._head._prev._date

    def append_front(self, date):
        self.insert(self.begin(), date)

    def append_back(self, date):
        self.insert(self.end(), date)

    def clear(self):
        self._head._prev = self._head._next = self._head

    def begin(self):
        return Coordinate(self._head._next)
    
    def end(self):
        return Coordinate(self._head._prev)

    def __len__(self):
        n = 0
        nodo = self._head._next
        while nodo is not self._head:
            n += 1
            nodo = nodo._next
        return n
    
    def insert(self, coord, date):
        aux = coord._node
        new = Nodo(date)
        new._prev = aux._prev
        new._next = aux
        new._prev._next = new
        new._next._prev = new
        self._size += 1
        return Coordinate(aux)

    def __eq__(self, other):
        p = self.begin()
        q = other.begin()
        while p != self.end() and q != other.end():
            if p.value != q.value:
                return False
            p.advance()
            q.advance()
        return p == self.end() and q == other.end()

    def __repr__(self):
        return 'DoublyLinkedList([' + ', '.join(repr(v) for v in self) + '])'

    def __iter__(self):
        return Iterator(self._head._next, self._head)

    def CoordinateMaker(self, index):
        assert not self.is_empty, 'Empty list'
        aux = self._head
        count = 0

        def valid_index(indx, max):
            return (indx >= 0 and indx < max)
        
        if (valid_index(index, len(self))):
            while aux is not None and count <= index:
                aux = aux._next
                count += 1
            return Coordinate(aux)


a = DoblyList()
a.append_front(5)
a.append_front(3)
a.append_front(2)
a.append_front(1)
coord = a.CoordinateMaker(3)
a.insert(coord,4)    
print(a)