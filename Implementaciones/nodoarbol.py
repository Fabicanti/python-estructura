class Nodo():

    __slots__ = ['_date', '_left','_rigth','_parent']

    def __init__(self, date = None):
        self._left = self._rigth = self._parent = None
        if date is not None:
            self._date = date
        else:
            self._date = None
        
