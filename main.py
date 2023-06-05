from claseColeccion import ManejadorEmpleados
if __name__ == '__main__':
    dimension = int(input('Ingrese la dimension del arreglo: '))
    empleados = ManejadorEmpleados(dimension, 5)
    empleados.setDimension(dimension)
    archivo = 'planta.csv'
    empleados.cargarArreglo(archivo)
    archivo = 'contratados.csv'
    empleados.cargarArreglo(archivo)
    archivo = 'externos.csv'
    empleados.cargarArreglo(archivo)
    empleados.mostrarArreglo()
    band = True
    while band == True:
        print('''
                Ingrese alguna de las siguientes opciones:')
                1: Incrementar y registrar la cantidad de horas trabajadas de un empleado contratado.
                2: Monto total a pagar por una tarea realizada por un empleado externo.
                3: Listar empleados de planta con sueldo inferior a $150000.
                4: Mostrar sueldo a cobrar de todos los empleados.
                '0: Salir del Menú
                ''')

        op = int(input('Ingrese una opción:'))

        if op == 0:
            band = False
            print('Gracias por utilizar nuestro servicio. Hasta pronto\n')

        elif op == 1:
            dni = input('Ingrese el dni de un empleado:')
            empleados.cantHorasTrabajo(dni)

        elif op == 2:
            tarea = input('Ingrese una tarea:')
            empleados.montoAPagar(tarea)

        elif op == 3:
            print('Empleados de Planta con sueldo menor a 150000: ')
            empleados.listarSueldoInferior()

        elif op == 4:
            empleados.mostrarSueldo()