import csv
import numpy as np
from claseEmpleado import Empleado
from claseDePlanta import Planta
from claseContratado import Contratado
from claseExterno import Externo

class ManejadorEmpleados:
    __cantidad= 0
    __dimension = 0    #tamaño
    __incremento = 5
    __arregloEmp = None

    def __init__(self, dimension, incremento):
        self.__cantidad = 0
        self.__dimension = dimension
        self.__incremento = incremento
        self.__arregloEmp = np.empty(dimension, dtype=Empleado)

    def setDimension(self, dimension):
        self.__dimension = dimension
        return self.__dimension

    def agregarArreglo(self, empleado):
        if self.__cantidad == self.__dimension:
            self.__dimension += self.__incremento
            self.__arregloEmp.resize(self.__dimension)
        self.__arregloEmp[self.__cantidad] = empleado
        self.__cantidad += 1

    def cargarArreglo(self, file):
        archivo = open(file, 'r')
        reader = csv.reader(archivo, delimiter=';')
        next(reader)
        for line in reader:
            if len(line) == 6:
                empleado = Planta(line[0], line[1], line[2], line[3], line[4], line[5])
                self.agregarArreglo(empleado)

            elif len(line) == 8:
                empleado = Contratado(line[0], line[1], line[2], line[3], line[4], line[5], line[6], line[7])
                self.agregarArreglo(empleado)

            elif len(line) == 10:
                empleado = Externo(line[0], line[1], line[2], line[3], line[4], line[5], line[6], line[7],
                                           line[8], line[9])
                self.agregarArreglo(empleado)
        archivo.close()

    def mostrarArreglo(self):
        for i in range(self.__cantidad):
            print(self.__arregloEmp[i])

    def cantHorasTrabajo(self, dni):
        i = 0
        band = False
        while i < len(self.__arregloEmp) and band == False:
            if dni == self.__arregloEmp[i].getDni():
                band = True
                cant = int(input('Ingrese la cantidad de horas que realizó el empleado en el día: '))
                self.__arregloEmp[i].setCantidadHoras(cant)
                print('Cantidad de horas acumuladas:', self.__arregloEmp[i].getCantidadHoras())
            else:
                i += 1
        if band == False:
            print('No se encuentra el dni ingresado, intente nuevamente')

    def montoAPagar(self, tarea):
        montoTotal = 0.0
        for i in range(len(self.__arregloEmp)):
            if isinstance(self.__arregloEmp[i], Externo):
                if tarea == self.__arregloEmp[i].getTarea() and str(2023/5/31) < str(self.__arregloEmp[i].getFin()):
                    montoTotal += float(self.__arregloEmp[i].getMontoViatico()) + float(self.__arregloEmp[i].getMontoSeguro())
                    print('El monto total:', montoTotal)

    def listarSueldoInferior(self):
        for i in range(len(self.__arregloEmp)):
            if isinstance(self.__arregloEmp[i],Planta):
                if self.__arregloEmp[i].getSueldo() < 150000:
                    print('Nombre: ', self.__arregloEmp[i].getNombre())
                    print('Dirección: ', self.__arregloEmp[i].getDireccion())
                    print('DNI: ', self.__arregloEmp[i].getDni())

    def mostrarSueldo(self):
        for i in range(len(self.__arregloEmp)):
            sueldo = 0.0
            if isinstance(self.__arregloEmp[i], Planta):
                sueldo = self.__arregloEmp[i].calculaSueldo()
                print(f'Nombre: {self.__arregloEmp[i].getNombre()}, Telefono: {self.__arregloEmp[i].getTelefono()}, Sueldo: {sueldo}')
            elif isinstance(self.__arregloEmp[i], Contratado):
                sueldo = self.__arregloEmp[i].calculaSueldo()
                print(f'Nombre: {self.__arregloEmp[i].getNombre()}, Telefono: {self.__arregloEmp[i].getTelefono()}, Sueldo: {sueldo}')
            elif isinstance(self.__arregloEmp[i], Externo):
                sueldo = self.__arregloEmp[i].calculaSueldo()
                print(f'Nombre: {self.__arregloEmp[i].getNombre()}, Telefono: {self.__arregloEmp[i].getTelefono()}, Sueldo: {sueldo}')