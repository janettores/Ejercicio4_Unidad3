from claseEmpleado import Empleado
class Contratado(Empleado):
    __fechaInicio: str
    __fechaFin: str
    __cantidadHoras: int
    __valorHora: float

    def __init__(self, dni, nombre, direccion, telefono, fechaInicio, fechaFin, cantidadHoras, valorHora):
        super().__init__(dni, nombre, direccion, telefono)
        self.__fechaInicio = fechaInicio
        self.__fechaFin = fechaFin
        self.__cantidadHoras = int(cantidadHoras)
        self.__valorHora = float(valorHora)

    def getInicio(self):
        return self.__fechaInicio

    def getFin(self):
        return self.__fechaFin

    def getCantidadHoras(self):
        return self.__cantidadHoras

    def getValorHora(self):
        return self.__valorHora

    def setCantidadHoras(self, cant):
        self.__cantidadHoras += cant
        return self.__cantidadHoras

    def calculaSueldo(self):
        sueldo = self.__cantidadHoras * self.__valorHora
        return sueldo