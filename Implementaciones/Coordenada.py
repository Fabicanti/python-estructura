import nododoble

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
        