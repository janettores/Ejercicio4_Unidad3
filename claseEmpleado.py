class Empleado:
    __dni: str
    __nombre: str
    __direccion: str
    __telefono: str

    def __init__(self, dni, nombre, direccion, telefono):
        self.__dni = dni
        self.__nombre = nombre
        self.__direccion = direccion
        self.__telefono = telefono

    def __str__(self):
        print('Empleado:')
        return f'DNI: {self.__dni}, Nombre: {self.__nombre}, Dirección: {self.__direccion}, Teléfono: {self.__telefono}'

    def getDni(self):
        return self.__dni

    def getNombre(self):
        return self.__nombre

    def getDireccion(self):
        return self.__direccion

    def getTelefono(self):
        return self.__telefono