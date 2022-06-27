class Nodo():

    __slots__ = ['_date', '_next', '_prev']
    
    def __init__(self,date):
        self._date = date
        self._next = self._prev = None

    def __repr__(self) -> str:
        return self._date

class Head():
    __slots__ = ['_prev','_next']

    def __init__(self):
        self._next = self._prev = Nodo(None)


class Coordinate():

    __slots__ = ['_node']

    def __init__(self, cordinate_node):
        if isinstance(cordinate_node, Coordinate):
            self._node = cordinate_node._node
        else:
            self._node = cordinate_node
    
    @property
    def value(self):
        return self._node._date

    @value.setter
    def value(self,date):
        self._node._date = date
    
    def advance(self):
        self._node = self._node._next
        return self
    
    def next(self):
        return Coordinate(self._node).advance()

    def retreat(self):
        self._node = self._node._prev
        return self

    def prev(self):
        return Coordinate(self._node).retreat()

    def __eq__(self,other):
        return self._node is other._node
        
class Iterator():

    __slots__ = ['_node', '_end']

    def __init__(self, head, end):
        self._node = head
        self._end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self._node is self._end:
            raise StopIteration
        value = self._node._date
        self._node = self._node._next
        return value
    
