class Fecha():
    __slots__ = ['_meses', '_values', '_dia', '_mes', '_anio']

    def __init__(self, value = 0):
        self._meses = [None, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        self._values = []
        if value != 0:
            self.setFecha(value)

    def eliminar(self):
        self._values = []

    def esBisiesto(self):
        return not self._anio % 4 and (self.anio % 100 or not self._anio % 400)

    def actualizarFecha(self):
        self._values = []
        self._values.append(self._dia)
        self._values.append(self._mes)
        self._values.append(self._anio)

    def validarFecha(self):
        if (self._mes >= 1 and self._mes <= 12):
            if self.esBisiesto():
                self._meses[2] = 29
            else:
                self._meses[2] = 28
            assert (self._dia <= self._meses[self._mes] and self._dia >= 1), 'Fecha invalida: El dia '+str(self._dia)+' se excede del permitido en el mes '+str(self._mes)+'(hasta '+str(self._meses[self._mes])+')'
        assert not (self._mes > 13 or self._mes < 0), 'Fecha invalida: El mes no es valido'

    def setFecha(self, value):
        assert (len(str(value)) == 8), 'Fecha Invalida, el formato debe ser DDMMAAAA'
        self._dia=(int(value)//1000000)%100
        self._mes=(int(value)//10000)%100
        self._anio=int(value)%10000
        self.validarFecha()
        self.actualizarFecha()

    def setDia(self,dd):
        self._dia = dd
        self.validarFecha()
        self.actualizarFecha()

    def setMes(self,mm):
        self._mes = mm
        self.validarFecha()
        self.actualizarFecha()

    def setaño(self,aaaa):
        self._anio = aaaa
        self.validarFecha()
        self.actualizarFecha()

    def getDia(self):
        return self._dia()
    
    def getMes(self):
        return self._mes()
    
    def getAño(self):
        return self._anio()

    def __repr__(self):
        return 'La fecha es: ('+ '/'.join(repr(x) for x in self._values)+ ')'

    def __eq__(self, other):
        return self._values==other._values

