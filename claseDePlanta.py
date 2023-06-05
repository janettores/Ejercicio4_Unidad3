from claseEmpleado import Empleado
class Planta(Empleado):
    __sueldoBasico: float
    __antiguedad: int

    def __init__(self, dni, nombre, direccion, telefono, sueldoBasico, antiguedad):
        super().__init__(dni, nombre, direccion, telefono)
        self.__sueldoBasico = float(sueldoBasico)
        self.__antiguedad = int(antiguedad)

    def getSueldo(self):
        return self.__sueldoBasico

    def getAntiguedad(self):
        return self.__antiguedad

    def calculaSueldo(self):
        sueldo = self.__sueldoBasico + (self.__sueldoBasico*0.01) * self.__antiguedad
        return sueldo