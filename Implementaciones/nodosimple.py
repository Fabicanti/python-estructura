class Nodo():
    __slots__ = ['_date', '_next']
    
    def __init__(self,date):
        self._date = date
        self._next = None

    def __repr__(self) -> str:
        return self._date

