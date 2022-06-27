import nodoarbol

class TreeDick():

    __slots__ = ['_root','_len']

    def __init__(self):
        self._root = nodoarbol.Nodo()
        self._len = 0

    @property
    def empty(self):
        return self._len == 0

    @property
    def __len__(self):
        return self._len

    def _add(self, nodo, date):
        if date < nodo._date:
            if nodo._left is None:
                nodo._left = nodoarbol.Nodo(date)
                self._len += 1
            else:
                self._add(nodo._left, date)
        if date > nodo._date:
            if nodo._rigth is None:
                nodo._rigth = nodoarbol.Nodo(date)
                self._len += 1
            else:
                self._add(nodo._rigth, date)
        
    
    def add(self, date):
        if self.empty:
            self._root._left = nodoarbol.Nodo(date)
            self._len += 1
        else:
            self._add(self._root._left, date)

    def _erase(self, nodo, date):
        if nodo._date == date:
            if (nodo._rigth and nodo._left) == None:
                self._len -= 1
        if date < nodo._date:
            self._erase(nodo._left, date)
        if date > nodo._date:
            self._erase(nodo._rigth, date)
    
    def erase(self, date):
        if self.empty:
            print("Empty Tree.")
        else:
            self._erase(self._root._left, date)


    def _orden(self, nodo):
        if nodo is not None:
            self._orden(nodo._left)
            print(nodo._date, end = ", ")
            self._orden(nodo._rigth)

    def in_orden(self):
        print("Tree inorden: ")
        self._orden(self._root)
        print("")



a = TreeDick()
a.add(10)
a.add(5)
a.add(4)
a.add(7)
a.add(2)
a.in_orden()
a.erase(4)
a.in_orden()