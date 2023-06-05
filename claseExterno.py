from claseEmpleado import Empleado
class Externo(Empleado):
    __tarea: str
    __fechaInicio: str
    __fechaFin: str
    __montoViatico: float
    __costoObra: float
    __montoSeguro: float

    def __init__(self, dni, nombre, direccion, telefono, tarea, fechaInicio, fechaFin, montoViatico, costoObra, montoSeguro):
        super().__init__(dni, nombre, direccion, telefono)
        self.__tarea = tarea
        self.__fechaInicio = fechaInicio
        self.__fechaFin = fechaFin
        self.__montoViatico = float(montoViatico)
        self.__costoObra = float(costoObra)
        self.__montoSeguro = float(montoSeguro)

    def getTarea(self):
        return self.__tarea

    def getInicio(self):
        return self.__fechaInicio

    def getFin(self):
        return self.__fechaFin

    def getMontoViatico(self):
        return self.__montoViatico

    def costoObra(self):
        return self.__costoObra

    def getMontoSeguro(self):
        return self.__montoSeguro

    def calculaSueldo(self):
        sueldo = self.__costoObra - self.__montoViatico - self.__montoSeguro
        return sueldo