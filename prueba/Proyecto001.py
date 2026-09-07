# ---------------- MENÚ PRINCIPAL ----------------
"""
Nombre: menuPrincipal
Entrada: No tiene
Salida: No retorna valores, ejecuta el menú principal del sistema
Restricciones:
    - El usuario debe ingresar una opción válida 1, 2 o 3
    - El menú se ejecuta de forma cíclica hasta que el usuario seleccione salir
    """
def menuPrincipal():
    while True:
        print("\n --- MENÚ PRINCIPAL --- ")
        print("1. Opciones Administrativas")
        print("2. Opciones de Usuario")
        print("3. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            accesoAdministrativo()
        elif opcion == "2":
            menuUsuario()
        elif opcion == "3":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida")


# ---------------- ACCESO ADMINISTRATIVO ----------------
"""
Nombre: accesoAdministrativo
Entrada: No tiene
Salida: No retorna valores, permite o deniega el acceso al menú administrativo
Restricciones:
    - El usuario debe ingresar una clave
    - La clave debe coincidir con alguna almacenada en el sistema
"""
def accesoAdministrativo():
    clave = input("Ingrese la clave de acceso: ")

    if claveValida(clave):
        menuAdministrativo()
    else:
        print("Clave Incorrecta")


# ---------------- MENÚ ADMINISTRATIVO ----------------
"""
Nombre: menuAdministrativo
Entrada: No tiene
Salida: No retorna valores, ejecuta el menú administrativo del sistema
Restricciones:
    - El usuario debe ingresar una opción válida 1 al 8
"""
def menuAdministrativo():
    while True:
        print("\n --- MENÚ ADMINISTRATIVO ---")
        print("1. Gestión de marcas de aviones")
        print("2. Gestión de modelos de aviones")
        print("3. Gestión de aerolíneas")
        print("4. Gestión de aviones por aerolínea")
        print("5. Gestión de vuelos")
        print("6. Consultar historial de reservaciones")
        print("7. Estadísticas de vuelo")
        print("8. Regresar al menú principal")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            menuGestionDeMarcasAviones()
        elif opcion == "2":
            menuGestionDeModelosAviones()
        elif opcion == "3":
            menuGestionDeAerolineas()
        elif opcion == "4":
            menuGestionDeAvionesAerolinea()
        elif opcion == "5":
            menuGestionDeVuelos()
        elif opcion == "6":
            menuHistorialReservaciones()
        elif opcion == "7":
            estadisticasVuelo()
        elif opcion == "8":
            print("Regresando al menú principal...")
            break
        else:
            print("Opción inválida")


# ---------------- MENÚ USUARIO ----------------
"""
Nombre: menuUsuario
Entrada: No tiene
Salida: No retorna valores, ejecuta el menú de usuario del sistema
Restricciones:
    - El usuario debe ingresar una opción válida 1 al 4
    - Cada opción debe dirigir correctamente a su respectiva funcionalidad
"""
def menuUsuario():
    while True:
        print("\n --- MENÚ USUARIO --- ")
        print("1. Consulta de vuelos")
        print("2. Reservación de vuelo")
        print("3. Cancelación de reservación")
        print("4. Regresar al menú principal")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            consultarVuelos()
        elif opcion == "2":
            reservarVuelo()
        elif opcion == "3":
            cancelarReservacion()
        elif opcion == "4":
            print("Regresando al Menú Principal...")
            break
        else:
            print("Opción invalida")


# ---------------- SUBMENÚS ----------------
"""
Nombre: menuGestionDeMarcasAviones
Entrada: No tiene
Salida: No retorna valores, ejecuta el menú de gestión de marcas de aviones
Restricciones:
    - El usuario debe ingresar una opción válida 1 al 5
"""

def menuGestionDeMarcasAviones():
    while True:
        print("\n ---MENÚ GESTIÓN DE MARCAS DE AVIONES---")
        print("1.Mostrar marcas de aviones")
        print("2.Incluir marca de avión")
        print("3.Modificar marca de avión")
        print("4.Eliminar marca de avión")
        print("5.Salir a menú administrativo")

        opcion = input("Seleccione una opción:")

        if opcion == "1":
            mostrarMarcas()
        elif opcion == "2":
            incluirMarca()
        elif opcion == "3":
            modificarMarca()
        elif opcion == "4":
            eliminarMarca()
        elif opcion == "5":
            break
        else:
            print("Opción invalida")

"""
Nombre: menuGestionDeModelosAviones
Entrada: No tiene
Salida: No retorna valores, ejecuta el menú de gestión de modelos de aviones
Restricciones:
    - El usuario debe ingresar una opción válida 1 al 5
"""
def menuGestionDeModelosAviones():
    while True:
        print("\n ---MENÚ GESTIÓN DE MODELOS DE AVIONES---")
        print("1. Mostrar modelos de aviones")
        print("2. Incluir modelo de avión")
        print("3. Modificar modelo de avión")
        print("4. Eliminar modelo de avión")
        print("5. Salir a menú administrativo")

        opcion = input("Seleccione una opción:")

        if opcion == "1":
            mostrarModelos()
        elif opcion == "2":
            incluirModelo()
        elif opcion == "3":
            modificarModelo()
        elif opcion == "4":
            eliminarModelo()
        elif opcion == "5":
            break
        else:
            print("Opción inválida")


"""
Nombre: menuGestionDeAerolineas
Entrada: No tiene
Salida: No retorna valores, ejecuta el menú de gestión de aerolíneas
Restricciones:
    - El usuario debe ingresar una opción válida 1 al 5
"""
def menuGestionDeAerolineas():
    while True:
        print("\n ---MENÚ GESTIÓN DE AEROLÍNEAS---")
        print("1. Mostrar aerolíneas")
        print("2. Incluir aerolínea")
        print("3. Modificar aerolínea")
        print("4. Eliminar aerolínea")
        print("5. Salir a menú administrativo")

        opcion = input("Seleccione una opción:")

        if opcion == "1":
            mostrarAerolineas()
        elif opcion == "2":
            incluirAerolinea()
        elif opcion == "3":
            modificarAerolinea()
        elif opcion == "4":
            eliminarAerolinea()
        elif opcion == "5":
            break
        else:
            print("Opción inválida")


"""
Nombre: menuGestionDeAvionesAerolinea
Entrada: No tiene
Salida: No retorna valores, ejecuta el menú de gestión de aviones por aerolínea
Restricciones:
    - El usuario debe ingresar una opción válida 1 al 5
"""
def menuGestionDeAvionesAerolinea():
    while True:
        print("\n ---MENÚ GESTIÓN DE AVIONES POR AEROLÍNEA---")
        print("1. Mostrar aviones por aerolínea")
        print("2. Incluir aviones por aerolínea")
        print("3. Modificar aviones por aerolínea")
        print("4. Eliminar aviones por aerolínea")
        print("5. Salir a menú administrativo")

        opcion = input("Seleccione una opción:")

        if opcion == "1":
            mostrarAviones()
        elif opcion == "2":
            incluirAvion()
        elif opcion == "3":
            modificarAvion()
        elif opcion == "4":
            eliminarAvion()
        elif opcion == "5":
            break
        else:
            print("Opción inválida")


"""
Nombre: menuGestionDeVuelos
Entrada: No tiene
Salida: No retorna valores, ejecuta el menú de gestión de vuelos
Restricciones:
    - El usuario debe ingresar una opción válida 1 al 5
"""
def menuGestionDeVuelos():
    while True:
        print("\n ---MENÚ GESTIÓN DE VUELOS---")
        print("1. Mostrar vuelos")
        print("2. Incluir vuelo")
        print("3. Modificar vuelo")
        print("4. Eliminar vuelo")
        print("5. Salir")

        opcion = input("Seleccione una opción:")

        if opcion == "1":
            mostrarVuelos()
        elif opcion == "2":
            incluirVuelo()
        elif opcion == "3":
            modificarVuelo()
        elif opcion == "4":
            eliminarVuelo()
        elif opcion == "5":
            break


"""
Nombre: menuHistorialReservaciones
Entrada: No tiene
Salida: No retorna valores, ejecuta el menú de historial de reservaciones
Restricciones:
    - El usuario debe ingresar una opción válida 1 al 3
"""
def menuHistorialReservaciones():
    while True:
        print("\n --- HISTORIAL DE RESERVACIONES ---")
        print("1. Mostrar todo")
        print("2. Filtrar")
        print("3. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            consultarHistorialReservaciones()
        elif opcion == "2":
            filtrarHistorialReservaciones()
        elif opcion == "3":
            break
        else:
            print("Opción inválida")

#--------------SUBMENU USUARIO--------------------
"""
Nombre: consultarVuelos
Entrada: No tiene
Salida: No retorna valores, ejecuta el submenú de consulta de vuelos
Restricciones:
    - El usuario debe ingresar una opción válida 1 al 3
"""
def consultarVuelos():

    while True:
        print("\n--- CONSULTA DE VUELOS ---")
        print("1. Ver todos los vuelos")
        print("2. Filtrar vuelos")
        print("3. Regresar")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            mostrarVuelosUsuario()
        elif opcion == "2":
            filtrarVuelos()
        elif opcion == "3":
            break
        else:
            print("Opción inválida")


# ---------------- CLAVE ACCESO ADMINISTRATIVO ----------------
"""
Nombre: claveValida
Entrada: claveIngresada 
Salida: True si la clave es válida, False en caso contrario
Restricciones:
    - claveIngresada debe ser string
    - El archivo "acceso.txt" debe existir
    - El archivo debe contener al menos una clave válida
"""
def claveValida(claveIngresada):
    archivo = open("acceso.txt","r")
    for linea in archivo:
        if claveIngresada == linea.strip():
            archivo.close()
            return True
    archivo.close()
    return False


# ---------------- Gestión de marcas aviones  ----------------
"""
Nombre: mostrarMarcas
Entrada: No tiene
Salida: Muestra en pantalla la lista de marcas de aviones
Restricciones:
    - El archivo "aviones.txt" debe existir
    - El archivo debe contener información de marcas
"""
def mostrarMarcas():
    archivo = open("aviones.txt","r")
    print("\n--- LISTA DE MARCAS ---")
    for linea in archivo:
        print(linea.strip())
    archivo.close()


"""
Nombre: incluirMarca
Entrada: No tiene
Salida: Agrega una nueva marca al archivo
Restricciones:
    - No se permiten marcas duplicadas
    - El archivo "aviones.txt" debe existir
"""
def incluirMarca():
    nuevaMarca = input("Ingrese nueva marca: ")

    archivo = open("aviones.txt","r")
    for linea in archivo:
        if nuevaMarca.lower() == linea.strip().lower():
            print("Esa marca ya existe")
            archivo.close()
            return
    archivo.close()

    archivo = open("aviones.txt","a")
    archivo.write(nuevaMarca + "\n")
    archivo.close()

    print("Marca agregada")

"""
Nombre: modificarMarca
Entrada: No tiene
Salida: Modifica una marca existente en el archivo
Restricciones:
    - El archivo "aviones.txt" debe existir
    - La marca a modificar debe existir en el archivo
"""
def modificarMarca():
    marcaVieja = input("Marca a modificar: ")
    nuevaMarca = input("Nueva marca: ")

    archivo = open("aviones.txt","r")
    contenidoLineas = archivo.readlines()
    archivo.close()

    archivo = open("aviones.txt","w")

    for linea in contenidoLineas:
        if linea.strip().lower() == marcaVieja.lower():
            archivo.write(nuevaMarca + "\n")
        else:
            archivo.write(linea)

    archivo.close()
    print("Marca modificada")


"""
Nombre: eliminarMarca
Entrada: No tiene
Salida: Elimina una marca del archivo
Restricciones:
    - El archivo "aviones.txt" y "modeloAviones.txt" deben existir
    - No se puede eliminar una marca si está asociada a un modelo
"""
def eliminarMarca():
    eliminar = input("Ingrese la marca a eliminar: ")

    archivo = open("modeloAviones.txt","r")
    for linea in archivo:
        datos = linea.strip().split(";")
        if eliminar.lower() == datos[1].lower():
            print("No se puede eliminar, la marca está asociada a un modelo")
            archivo.close()
            return
    archivo.close()

    archivo = open("aviones.txt","r")
    contenidoLineas = archivo.readlines()
    archivo.close()

    archivo = open("aviones.txt","w")

    for linea in contenidoLineas:
        if eliminar.lower() != linea.strip().lower():
            archivo.write(linea)

    archivo.close()
    print("Marca eliminada")


# ---------------- Gestión de modelos de aviones  ----------------
"""
Nombre: mostrarModelos
Entrada: No tiene
Salida: Muestra en pantalla la lista de modelos de aviones
Restricciones:
    - El archivo "modeloAviones.txt" debe existir
    - El archivo debe contener información de modelos
"""
def mostrarModelos():
    archivo = open("modeloAviones.txt","r")
    print("\n--- LISTA DE MODELOS ---")
    for linea in archivo:
        print(linea.strip())
    archivo.close()


"""
Nombre: incluirModelo
Entrada: No tiene
Salida: Agrega un nuevo modelo de avión al archivo
Restricciones:
    - No se permiten modelos duplicados
    - La marca ingresada debe existir en "aviones.txt"
    - Los archivos "modeloAviones.txt" y "aviones.txt" deben existir
"""
def incluirModelo():
    modelo = input("Descripción del modelo: ")

    # VALIDAR MODELO REPETIDO
    archivo = open("modeloAviones.txt","r")
    for linea in archivo:
        if modelo.lower() == linea.split(";")[0].lower():
            print("Ese modelo ya existe")
            archivo.close()
            return
    archivo.close()

    # MOSTRAR MARCAS DISPONIBLES
    print("\nMarcas disponibles:")
    archivo = open("aviones.txt","r")
    for linea in archivo:
        print(linea.strip())
    archivo.close()

    marca = input("Marca: ")
    ejecutiva = input("Asientos ejecutivos: ")
    turista = input("Asientos turistas: ")
    economico = input("Asientos económicos: ")

    # VALIDAR QUE LA MARCA EXISTA
    archivo = open("aviones.txt","r")
    existe = False
    for linea in archivo:
        if marca.lower() == linea.strip().lower():
            existe = True
    archivo.close()

    if not existe:
        print("La marca no existe")
        return

    archivo = open("modeloAviones.txt","a")
    archivo.write(modelo+";"+marca+";"+ejecutiva+";"+turista+";"+economico+"\n")
    archivo.close()

    print("Modelo agregado")


"""
Nombre: modificarModelo
Entrada: No tiene
Salida: Modifica un modelo existente en el archivo
Restricciones:
    - El modelo a modificar debe existir
    - La nueva marca debe existir en "aviones.txt"
    - Los archivos necesarios deben existir
"""
def modificarModelo():
    modeloViejo = input("Modelo a modificar: ")

    archivo = open("modeloAviones.txt","r")
    contenidoLineas = archivo.readlines()
    archivo.close()

    archivo = open("modeloAviones.txt","w")

    encontrado = False   

    for linea in contenidoLineas:
        datos = linea.strip().split(";")

        if datos[0].lower() == modeloViejo.lower():
            encontrado = True  

            modelo = input("Nuevo modelo: ")

            print("\nMarcas disponibles:")
            archivoMarcas = open("aviones.txt","r")
            for lineaMarca in archivoMarcas:
                print(lineaMarca.strip())
            archivoMarcas.close()

            marca = input("Nueva marca: ")
            ejecutiva = input("Asientos Ejecutivos: ")
            turista = input("Asientos Turista: ")
            economico = input("Asientos Económicos: ")

            # VALIDAR MARCA
            archivoMarcas = open("aviones.txt","r")
            existe = False
            for lineaMarca in archivoMarcas:
                if marca.lower() == lineaMarca.strip().lower():
                    existe = True
            archivoMarcas.close()

            if not existe:
                print("La marca no existe")
                archivo.write(linea)
            else:
                archivo.write(modelo+";"+marca+";"+ejecutiva+";"+turista+";"+economico+"\n")
        else:
            archivo.write(linea)

    archivo.close()

    if encontrado:
        print("Modelo modificado")
    else:
        print("Ese modelo no existe")


"""
Nombre: eliminarModelo
Entrada: No tiene
Salida: Elimina un modelo del archivo
Restricciones:
    - No se puede eliminar si está asociado a un avión
    - Los archivos "modeloAviones.txt" y "avionesAerolineas.txt" deben existir
"""
def eliminarModelo():
    eliminar = input("Ingrese el  modelo a eliminar: ")

    # VALIDAR SI ESTÁ ASOCIADO A UN AVIÓN
    archivo = open("avionesAerolineas.txt","r")
    for linea in archivo:
        datos = linea.strip().split(";")

        if eliminar.lower() == datos[2].lower():
            print("No se puede eliminar, el modelo está asociado a un avión")
            archivo.close()
            return
    archivo.close()

    archivo = open("modeloAviones.txt","r")
    contenidoLineas = archivo.readlines()
    archivo.close()

    archivo = open("modeloAviones.txt","w")

    for linea in contenidoLineas:
        if eliminar.lower() != linea.split(";")[0].lower():
            archivo.write(linea)

    archivo.close()
    print("Modelo eliminado")


# ---------------- Gestión de aerolíneas  ----------------
"""
Nombre: mostrarAerolineas
Entrada: No tiene
Salida: Muestra en pantalla la lista de aerolíneas registradas
Restricciones:
    - El archivo "aerolineas.txt" debe existir
"""
def mostrarAerolineas():
    archivo = open("aerolineas.txt","r")
    print("\n--- LISTA DE AEROLÍNEAS ---")
    for linea in archivo:
        print(linea.strip())
    archivo.close()

"""
Nombre: incluirAerolinea
Entrada: No tiene
Salida: Agrega una nueva aerolínea al archivo
Restricciones:
    - No se permiten aerolíneas duplicadas
"""
def incluirAerolinea():
    nombre = input("Nombre de la aerolínea: ")
    centro = input("Centro de operaciones: ")

    archivo = open("aerolineas.txt","r")

    for linea in archivo:
        datos = linea.strip().split(";")
        if nombre.lower() == datos[0].lower():
            print("Esa aerolínea ya existe")
            archivo.close()
            return

    archivo.close()

    archivo = open("aerolineas.txt","a")
    archivo.write(nombre+";"+centro+"\n")
    archivo.close()

    print("Aerolínea agregada")


"""
Nombre: modificarAerolinea
Entrada: No tiene
Salida: Modifica una aerolínea existente en el archivo
Restricciones:
    - La aerolínea a modificar debe existir en el archivo
"""
def modificarAerolinea():
    nombreViejo = input("Aerolínea a modificar: ")

    archivo = open("aerolineas.txt","r")
    contenidoLineas = archivo.readlines()
    archivo.close()

    archivo = open("aerolineas.txt","w")

    encontrado = False

    for linea in contenidoLineas:
        datos = linea.strip().split(";")

        if datos[0].lower() == nombreViejo.lower():
            encontrado = True

            nombre = input("Nuevo nombre: ")
            centro = input("Nuevo centro de operaciones: ")

            archivo.write(nombre+";"+centro+"\n")
        else:
            archivo.write(linea)

    archivo.close()

    if encontrado:
        print("Aerolínea modificada")
    else:
        print("Esa aerolínea no existe")

"""
Nombre: eliminarAerolinea
Entrada: No tiene
Salida: Elimina una aerolínea del archivo
Restricciones:
    - No se puede eliminar si está asociada a un avión
    """
def eliminarAerolinea():
    eliminar = input("Ingrese la aerolínea a eliminar: ")

    # VALIDAR SI ESTÁ ASOCIADA A UN AVIÓN
    archivo = open("avionesAerolineas.txt","r")
    for linea in archivo:
        datos = linea.strip().split(";")

        if eliminar.lower() == datos[4].lower():
            print("No se puede eliminar, la aerolínea está asociada a un avión")
            archivo.close()
            return
    archivo.close()

    archivo = open("aerolineas.txt","r")
    contenidoLineas = archivo.readlines()
    archivo.close()

    existe = False

    for linea in contenidoLineas:
        datos = linea.strip().split(";")
        if eliminar.lower() == datos[0].lower():
            existe = True

    if not existe:
        print("La aerolínea no existe")
        return

    archivo = open("aerolineas.txt","w")

    for linea in contenidoLineas:
        datos = linea.strip().split(";")
        if eliminar.lower() != datos[0].lower():
            archivo.write(linea)

    archivo.close()
    print("Aerolínea eliminada")


# ---------------- Gestión de aviones por aerolíneas ----------------
"""
Nombre: mostrarAviones
Entrada: No tiene
Salida: Muestra en pantalla la lista de aviones por aerolínea
Restricciones:
"""
def mostrarAviones():
    archivo = open("avionesAerolineas.txt","r")
    print("\n--- LISTA DE AVIONES --")
    for linea in archivo:
        print(linea.strip())
    archivo.close()


"""
Nombre: incluirAvion
Entrada: No tiene
Salida: Agrega un nuevo avión al archivo de aviones por aerolínea
Restricciones:
    - La matrícula no puede estar repetida
    - El modelo debe existir y pertenecer a la marca en "modeloAviones.txt"
"""
def incluirAvion():

    matricula = input("Matrícula: ")

    archivo = open("avionesAerolineas.txt","r")
    for linea in archivo:
        if matricula.lower() == linea.split(";")[0].lower():
            print("Esa matrícula ya existe")
            archivo.close()
            return
    archivo.close()

    # MOSTRAR MARCAS
    print("\nMarcas disponibles:")
    archivo = open("aviones.txt","r")
    for linea in archivo:
        print(linea.strip())
    archivo.close()

    marca = input("Marca: ")

    # VALIDAR MARCA
    archivo = open("aviones.txt","r")
    existeMarca = False
    for linea in archivo:
        if marca.lower() == linea.strip().lower():
            existeMarca = True
    archivo.close()

    if not existeMarca:
        print("La marca no existe")
        return

    # MOSTRAR MODELOS FILTRADOS
    print("\nModelos disponibles:")
    archivo = open("modeloAviones.txt","r")
    for linea in archivo:
        datos = linea.strip().split(";")
        if marca.lower() == datos[1].lower():
            print(datos[0])
    archivo.close()

    modelo = input("Modelo: ")

    # VALIDAR MODELO
    archivo = open("modeloAviones.txt","r")
    existeModelo = False
    for linea in archivo:
        datos = linea.strip().split(";")
        if modelo.lower() == datos[0].lower() and marca.lower() == datos[1].lower():
            existeModelo = True
    archivo.close()

    if not existeModelo:
        print("Modelo no válido para esa marca")
        return

    anio = input("Año: ")

    # MOSTRAR AEROLÍNEAS
    print("\nAerolíneas disponibles:")
    archivo = open("aerolineas.txt","r")
    for linea in archivo:
        print(linea.split(";")[0])
    archivo.close()

    aerolinea = input("Aerolínea: ")

    # VALIDAR AEROLÍNEA
    archivo = open("aerolineas.txt","r")
    existeAerolinea = False
    for linea in archivo:
        if aerolinea.lower() == linea.split(";")[0].lower():
            existeAerolinea = True
    archivo.close()

    if not existeAerolinea:
        print("La aerolínea no existe")
        return

    archivo = open("avionesAerolineas.txt","a")
    archivo.write("\n"+matricula+";"+marca+";"+modelo+";"+anio+";"+aerolinea)
    archivo.close()

    print("Avión agregado")

"""
Nombre: modificarAvion
Entrada: No tiene
Salida: Modifica un avión existente en el archivo
Restricciones:
    - La matrícula a modificar debe existir
"""
def modificarAvion():
    matriculaVieja = input("Matrícula a modificar: ")

    archivo = open("avionesAerolineas.txt","r")
    contenidoLineas = archivo.readlines()
    archivo.close()

    archivo = open("avionesAerolineas.txt","w")

    encontrado = False

    for linea in contenidoLineas:
        datos = linea.strip().split(";")

        if datos[0].lower() == matriculaVieja.lower():
            encontrado = True

            matricula = input("Nueva matrícula: ")
            marca = input("Marca: ")
            modelo = input("Modelo: ")
            anio = input("Año: ")
            aerolinea = input("Aerolínea: ")

            archivo.write("\n"+matricula+";"+marca+";"+modelo+";"+anio+";"+aerolinea)
        else:
            archivo.write(linea)

    archivo.close()

    if encontrado:
        print("Avión modificado")
    else:
        print("Ese avión no existe")


"""
Nombre: eliminarAvion
Entrada: No tiene
Salida: Elimina un avión del archivo
Restricciones:
    - No se puede eliminar si está asociado a un vuelo
"""
def eliminarAvion():
    eliminar = input("Ingrese la matrícula del avión a eliminar: ")

    # VALIDAR SI ESTÁ EN VUELOS
    archivo = open("vuelos.txt","r")
    for linea in archivo:
        datos = linea.strip().split(";")

        if eliminar.lower() == datos[8].lower():
            print("No se puede eliminar, el avión está registrado en vuelos")
            archivo.close()
            return
    archivo.close()

    archivo = open("avionesAerolineas.txt","r")
    contenidoLineas = archivo.readlines()
    archivo.close()

    archivo = open("avionesAerolineas.txt","w")

    for linea in contenidoLineas:
        if eliminar.lower() != linea.split(";")[0].lower():
            archivo.write(linea)

    archivo.close()
    print("Avión eliminado")

#------------------Gestión de vuelos---------------
"""
Nombre: generarNumeroVuelo
Entrada: No tiene
Salida: Retorna un string con el número de vuelo generado
Restricciones:
    - El número de vuelo se genera automáticamente
"""
def generarNumeroVuelo():
    archivo = open("vuelos.txt","r")
    contador = 0

    for linea in archivo:
        contador += 1

    archivo.close()

    return "AV" + str(250 + contador)

"""
Nombre: mostrarVuelos
Entrada: No tiene
Salida: Muestra en pantalla la lista de vuelos registrados
Restricciones:
"""
def mostrarVuelos():
    archivo = open("vuelos.txt","r")

    print("\n--- LISTA DE VUELOS ---")
    for linea in archivo:
        print(linea.strip())

    archivo.close()

"""
Nombre: incluirVuelo
Entrada: No tiene
Salida: Agrega un nuevo vuelo al archivo
Restricciones:
    - La aerolínea debe existir en "aerolineas.txt"
    - La matrícula debe existir y pertenecer a la aerolínea en "avionesAerolineas.txt"
    - El archivo "vuelos.txt" debe existir
"""
def incluirVuelo():
    numeroVuelo = generarNumeroVuelo()

    print("Número de vuelo generado:", numeroVuelo)

    codigoSalida = input("Código aeropuerto salida: ")
    fechaSalida = input("Fecha salida (dd/mm/aaaa): ")
    horaSalida = input("Hora salida: ")

    codigoLlegada = input("Código aeropuerto llegada: ")
    fechaLlegada = input("Fecha llegada (dd/mm/aaaa): ")
    horaLlegada = input("Hora llegada: ")

    # MOSTRAR AEROLÍNEAS
    print("\nAerolíneas disponibles:")
    archivo = open("aerolineas.txt","r")
    for linea in archivo:
        print(linea.split(";")[0])
    archivo.close()

    aerolinea = input("Seleccione aerolínea: ")

    # VALIDAR AEROLÍNEA
    archivo = open("aerolineas.txt","r")
    existeAerolinea = False
    for linea in archivo:
        if aerolinea.lower() == linea.split(";")[0].lower():
            existeAerolinea = True
    archivo.close()

    if not existeAerolinea:
        print("La aerolínea no existe")
        return

    # MOSTRAR AVIONES DE ESA AEROLÍNEA
    print("\nAviones disponibles para esa aerolínea:")
    archivo = open("avionesAerolineas.txt","r")
    for linea in archivo:
        datos = linea.strip().split(";")
        if aerolinea.lower() == datos[4].lower():
            print(datos[0])
    archivo.close()

    matricula = input("Seleccione matrícula del avión: ")

    # VALIDAR MATRÍCULA
    archivo = open("avionesAerolineas.txt","r")
    existeAvion = False
    for linea in archivo:
        datos = linea.strip().split(";")
        if matricula.lower() == datos[0].lower() and aerolinea.lower() == datos[4].lower():
            existeAvion = True
    archivo.close()

    if not existeAvion:
        print("El avión no existe para esa aerolínea")
        return

    montoEjecutiva = input("Monto clase ejecutiva: ")
    montoTurista = input("Monto clase turista: ")
    montoEconomico = input("Monto clase económica: ")

    # GUARDAR
    archivo = open("vuelos.txt","a")
    archivo.write("\n"+numeroVuelo+";"+codigoSalida+";"+fechaSalida+";"+horaSalida+";"+codigoLlegada+";"+fechaLlegada+";"+horaLlegada+";"+
                  aerolinea+";"+matricula+";"+ montoEjecutiva+";"+montoTurista+";"+montoEconomico)
    archivo.close()

    print("Vuelo agregado")


"""
Nombre: modificarVuelo
Entrada: No tiene
Salida: Modifica un vuelo existente en el archivo
Restricciones:
    - El número de vuelo debe existir
"""
def modificarVuelo():
    numeroVuelo = input("Ingrese número de vuelo a modificar: ")

    archivo = open("vuelos.txt","r")
    contenidoLineas = archivo.readlines()
    archivo.close()

    archivo = open("vuelos.txt","w")

    encontrado = False

    for linea in contenidoLineas:
        datos = linea.strip().split(";")

        if numeroVuelo.lower() == datos[0].lower():
            encontrado = True

            codigoSalida = input("Código salida: ")
            fechaSalida = input("Fecha salida: ")
            horaSalida = input("Hora salida: ")

            codigoLlegada = input("Código llegada: ")
            fechaLlegada = input("Fecha llegada: ")
            horaLlegada = input("Hora llegada: ")

            aerolinea = input("Aerolínea: ")
            matricula = input("Matrícula: ")

            montoEjecutiva = input("Monto ejecutiva: ")
            montoTurista = input("Monto turista: ")
            montoEconomico = input("Monto económico: ")

            archivo.write("\n"+numeroVuelo+";"+codigoSalida+";"+fechaSalida+";"+horaSalida+";"+ codigoLlegada+";"+fechaLlegada+";"+horaLlegada+";"+
                          aerolinea+";"+matricula+";"+ montoEjecutiva+";"+montoTurista+";"+montoEconomico)
        else:
            archivo.write(linea)

    archivo.close()

    if encontrado:
        print("Vuelo modificado")
    else:
        print("Ese vuelo no existe")
        
"""
Nombre: eliminarVuelo
Entrada: No tiene
Salida: Elimina un vuelo del archivo
Restricciones: El vuelo debe existir
"""
def eliminarVuelo():
    eliminarVuelo = input("Ingrese número de vuelo a eliminar: ")

    archivo = open("vuelos.txt","r")
    contenidoLineas = archivo.readlines()
    archivo.close()

    existe = False

    for linea in contenidoLineas:
        if eliminarVuelo.lower() == linea.split(";")[0].lower():
            existe = True

    if not existe:
        print("El vuelo no existe")
        return

    archivo = open("vuelos.txt","w")

    for linea in contenidoLineas:
        if eliminarVuelo.lower() != linea.split(";")[0].lower():
            archivo.write(linea)

    archivo.close()

    print("Vuelo eliminado")

#-------------Consultar historial de reservaciones---------------
"""
Nombre: consultarHistorialReservaciones
Entrada: No tiene
Salida: Muestra en pantalla el historial completo de reservaciones registradas
Restricciones:
"""
def consultarHistorialReservaciones():

    archivo = open("reservas.txt","r")

    print("\n--- HISTORIAL DE RESERVACIONES ---")

    for linea in archivo:

        if linea.strip() != "":

            datos = linea.strip().split(";")

            print("\nID:", datos[0])
            print("Nombre:", datos[1])
            print("Vuelo:", datos[2])

            print("Fecha reservación:", datos[3])
            print("Hora reservación:", datos[4])

            print("Aerolínea:", datos[5])
            print("Avión:", datos[6])

            print("Lugar salida:", datos[7])
            print("Fecha salida:", datos[8])
            print("Hora salida:", datos[9])

            print("Lugar llegada:", datos[10])
            print("Fecha llegada:", datos[11])
            print("Hora llegada:", datos[12])

            print("Ejecutiva:", datos[13])
            print("Turista:", datos[14])
            print("Económica:", datos[15])

            print("Total:", datos[16])

    archivo.close()

"""
Nombre: filtrarHistorialReservaciones
Entrada: No tiene
Salida: Muestra en pantalla las reservaciones que cumplen con los filtros ingresados
Restricciones:
    - Si el usuario presiona ENTER, el filtro se ignora
"""
def filtrarHistorialReservaciones():

    archivo = open("reservas.txt","r")
    lineas = archivo.readlines()
    archivo.close()

    print("\n--- FILTROS HISTORIAL ---")

    salidaFiltro = input("Lugar salida (ENTER para ignorar): ")
    llegadaFiltro = input("Lugar llegada (ENTER para ignorar): ")

    fechaSalidaInicio = input("Fecha salida desde (dd/mm/aaaa o ENTER): ")
    fechaSalidaFin = input("Fecha salida hasta (dd/mm/aaaa o ENTER): ")

    fechaLlegadaInicio = input("Fecha llegada desde (dd/mm/aaaa o ENTER): ")
    fechaLlegadaFin = input("Fecha llegada hasta (dd/mm/aaaa o ENTER): ")

    fechaReservaInicio = input("Fecha reservación desde (dd/mm/aaaa o ENTER): ")
    fechaReservaFin = input("Fecha reservación hasta (dd/mm/aaaa o ENTER): ")

    print("\n--- RESULTADOS ---")

    for linea in lineas:

        if linea.strip() != "":

            datos = linea.strip().split(";")

            fechaReserva = datos[3]

            lugarSalida = datos[7]
            fechaSalida = datos[8]

            lugarLlegada = datos[10]
            fechaLlegada = datos[11]

            mostrar = True  

            # ---------------- filtros ----------------
            if salidaFiltro != "" and salidaFiltro.lower() != lugarSalida.lower():
                mostrar = False

            if llegadaFiltro != "" and llegadaFiltro.lower() != lugarLlegada.lower():
                mostrar = False

            if fechaSalidaInicio != "" and fechaSalida < fechaSalidaInicio:
                mostrar = False

            if fechaSalidaFin != "" and fechaSalida > fechaSalidaFin:
                mostrar = False

            if fechaLlegadaInicio != "" and fechaLlegada < fechaLlegadaInicio:
                mostrar = False

            if fechaLlegadaFin != "" and fechaLlegada > fechaLlegadaFin:
                mostrar = False

            if fechaReservaInicio != "" and fechaReserva < fechaReservaInicio:
                mostrar = False

            if fechaReservaFin != "" and fechaReserva > fechaReservaFin:
                mostrar = False

            if mostrar == True:

                print("\nID:", datos[0])
                print("Nombre:", datos[1])
                print("Vuelo:", datos[2])

                print("Fecha reservación:", datos[3])
                print("Hora reservación:", datos[4])

                print("Aerolínea:", datos[5])
                print("Avión:", datos[6])

                print("Lugar salida:", datos[7])
                print("Fecha salida:", datos[8])
                print("Hora salida:", datos[9])

                print("Lugar llegada:", datos[10])
                print("Fecha llegada:", datos[11])
                print("Hora llegada:", datos[12])

                print("Ejecutiva:", datos[13])
                print("Turista:", datos[14])
                print("Económica:", datos[15])

                print("Total:", datos[16])
#----------------------Estadísticas de vuelo---------------------
"""
Nombre: estadisticasVuelo
Entrada: No tiene
Salida: Muestra estadísticas detalladas de un vuelo específico
Restricciones:
    - El número de vuelo debe existir en el sistema
"""
def estadisticasVuelo():

    mostrarVuelos()

    numeroVuelo = input("Seleccione número de vuelo: ")

    #------------------BUSCAR VUELO------------------
    archivo = open("vuelos.txt","r")
    encontrado = False

    for linea in archivo:

        if linea.strip() != "":

            datos = linea.strip().split(";")

            if numeroVuelo.lower() == datos[0].lower():
                encontrado = True

                codigoSalida = datos[1]
                fechaSalida = datos[2]
                horaSalida = datos[3]

                codigoLlegada = datos[4]
                fechaLlegada = datos[5]
                horaLlegada = datos[6]

                aerolinea = datos[7]
                matricula = datos[8]

                montoEjecutiva = int(datos[9])
                montoTurista = int(datos[10])
                montoEconomico = int(datos[11])

    archivo.close()

    if not encontrado:
        print("El vuelo no existe")
        return


    #------------------ASIENTOS RESERVADOS------------------
    totalEjecutiva = 0
    totalTurista = 0
    totalEconomica = 0
    montoRecaudado = 0

    archivo = open("reservas.txt","r")

    for linea in archivo:

        if linea.strip() != "":

            datos = linea.strip().split(";")

            if numeroVuelo.lower() == datos[2].lower():

                totalEjecutiva += int(datos[13])
                totalTurista += int(datos[14])
                totalEconomica += int(datos[15])

                montoRecaudado += int(datos[16])

    archivo.close()


    #------------------BUSCAR CAPACIDAD DEL AVIÓN------------------
    archivo = open("avionesAerolineas.txt","r")

    marca = ""
    modelo = ""

    for linea in archivo:

        if linea.strip() != "":

            datos = linea.strip().split(";")

            if matricula.lower() == datos[0].lower():
                marca = datos[1]
                modelo = datos[2]

    archivo.close()


    archivo = open("modeloAviones.txt","r")

    capacidadEjecutiva = 0
    capacidadTurista = 0
    capacidadEconomica = 0

    for linea in archivo:

        if linea.strip() != "":

            datos = linea.strip().split(";")

            if modelo.lower() == datos[0].lower() and marca.lower() == datos[1].lower():
                capacidadEjecutiva = int(datos[2])
                capacidadTurista = int(datos[3])
                capacidadEconomica = int(datos[4])

    archivo.close()


    #------------------DISPONIBLES------------------
    disponiblesEjecutiva = capacidadEjecutiva - totalEjecutiva
    disponiblesTurista = capacidadTurista - totalTurista
    disponiblesEconomica = capacidadEconomica - totalEconomica


    #------------------MOSTRAR RESULTADO------------------
    print("\n--- ESTADÍSTICAS DEL VUELO ---")

    print("Vuelo:", numeroVuelo)
    print("Aerolínea:", aerolinea)
    print("Avión:", matricula)

    print("\nLugar salida:", codigoSalida)
    print("Fecha salida:", fechaSalida)
    print("Hora salida:", horaSalida)

    print("\nLugar llegada:", codigoLlegada)
    print("Fecha llegada:", fechaLlegada)
    print("Hora llegada:", horaLlegada)

    print("\n--- ASIENTOS ---")

    print("Ejecutiva reservados:", totalEjecutiva)
    print("Ejecutiva disponibles:", disponiblesEjecutiva)

    print("Turista reservados:", totalTurista)
    print("Turista disponibles:", disponiblesTurista)

    print("Económica reservados:", totalEconomica)
    print("Económica disponibles:", disponiblesEconomica)

    print("\n--- COSTOS ---")

    print("Ejecutiva:", montoEjecutiva)
    print("Turista:", montoTurista)
    print("Económica:", montoEconomico)

    print("\nMonto total recaudado:", montoRecaudado)


#Opciones de Usuario

#---------------Consulta vuelos------------------------------
"""
Nombre: mostrarVuelosUsuario
Entrada: No tiene
Salida: Muestra en pantalla la lista de vuelos disponibles para el usuario
Restricciones:
"""
def mostrarVuelosUsuario():

    archivo = open("vuelos.txt","r")

    print("\n--- LISTA DE VUELOS ---")

    for linea in archivo:

        if linea.strip() != "":

            datos = linea.strip().split(";")

            print("\nVuelo:", datos[0])
            print("Aerolínea:", datos[7])
            print("Avión:", datos[8])
            print("Salida:", datos[1], datos[2], datos[3])
            print("Llegada:", datos[4], datos[5], datos[6])
            print("Ejecutiva:", datos[9])
            print("Turista:", datos[10])
            print("Económica:", datos[11])

    archivo.close()

"""
Nombre: filtrarVuelos
Entrada: No tiene
Salida: Muestra vuelos que cumplen con los filtros ingresados
Restricciones:
"""
def filtrarVuelos():

    archivo = open("vuelos.txt","r")
    lineas = archivo.readlines()
    archivo.close()

    print("\n--- FILTROS ---")

    aerolineaFiltro = input("Aerolínea (ENTER para ignorar): ")
    salidaFiltro = input("Lugar salida (ENTER para ignorar): ")
    llegadaFiltro = input("Lugar llegada (ENTER para ignorar): ")

    fechaSalidaInicio = input("Fecha salida desde (dd/mm/aaaa o ENTER): ")
    fechaSalidaFin = input("Fecha salida hasta (dd/mm/aaaa o ENTER): ")

    fechaLlegadaInicio = input("Fecha llegada desde (dd/mm/aaaa o ENTER): ")
    fechaLlegadaFin = input("Fecha llegada hasta (dd/mm/aaaa o ENTER): ")

    print("\n--- RESULTADOS ---")

    for linea in lineas:

        if linea.strip() != "":

            datos = linea.strip().split(";")

            numero = datos[0]
            salida = datos[1]
            fechaSalida = datos[2]
            horaSalida = datos[3]

            llegada = datos[4]
            fechaLlegada = datos[5]
            horaLlegada = datos[6]

            aerolinea = datos[7]
            avion = datos[8]

            montoE = datos[9]
            montoT = datos[10]
            montoEco = datos[11]

            # ---------------- BANDERA DE CONTROL ----------------
            mostrar = True

            if aerolineaFiltro != "" and aerolineaFiltro.lower() != aerolinea.lower():
                mostrar = False

            if salidaFiltro != "" and salidaFiltro.lower() != salida.lower():
                mostrar = False

            if llegadaFiltro != "" and llegadaFiltro.lower() != llegada.lower():
                mostrar = False

            if fechaSalidaInicio != "" and fechaSalida < fechaSalidaInicio:
                mostrar = False

            if fechaSalidaFin != "" and fechaSalida > fechaSalidaFin:
                mostrar = False

            if fechaLlegadaInicio != "" and fechaLlegada < fechaLlegadaInicio:
                mostrar = False

            if fechaLlegadaFin != "" and fechaLlegada > fechaLlegadaFin:
                mostrar = False

            # ---------------- IMPRESIÓN FINAL ----------------
            if mostrar == True:

                print("\nVuelo:", numero)
                print("Aerolínea:", aerolinea)
                print("Avión:", avion)
                print("Salida:", salida, fechaSalida, horaSalida)
                print("Llegada:", llegada, fechaLlegada, horaLlegada)
                print("Ejecutiva:", montoE)
                print("Turista:", montoT)
                print("Económica:", montoEco)
    
#------------------Reservación de vuelo----------------------
"""
Nombre: generarIdReservacion
Entrada: No tiene
Salida: Retorna un string con el identificador de reservación generado auromaticamente
Restricciones:
    - El identificador se genera automáticamente 
"""
def generarIdReservacion():
    archivo = open("reservas.txt","r")
    contador = 0

    for linea in archivo:
        if linea.strip() != "":
            contador += 1

    archivo.close()

    return "R" + str(contador + 1)

"""
Nombre: reservarVuelo
Entrada: No tiene
Salida: Registra una nueva reservación y muestra el comprobante
Restricciones:
    - El vuelo debe existir en "vuelos.txt"
    - Los archivos necesarios deben existir
    - Las cantidades de asientos deben ser números enteros
    - No se permite reservar 0 asientos
    - No se pueden exceder las capacidades del avión
"""
def reservarVuelo():

    nombre = input("Nombre de la persona: ")

    mostrarVuelos()

    numeroVuelo = input("Seleccione número de vuelo: ")

    #------------------BUSCAR VUELO------------------
    archivo = open("vuelos.txt","r")
    encontrado = False

    for linea in archivo:
        datos = linea.strip().split(";")

        if numeroVuelo.lower() == datos[0].lower():
            encontrado = True

            codigoSalida = datos[1]
            fechaSalida = datos[2]
            horaSalida = datos[3]

            codigoLlegada = datos[4]
            fechaLlegada = datos[5]
            horaLlegada = datos[6]

            aerolinea = datos[7]
            matricula = datos[8]

            montoEjecutiva = int(datos[9])
            montoTurista = int(datos[10])
            montoEconomico = int(datos[11])

    archivo.close()

    if not encontrado:
        print("Este vuelo no existe")
        return


    #------------------CANTIDAD DE ASIENTOS------------------
    cantEjecutiva = int(input("Asientos ejecutiva: "))
    cantTurista = int(input("Asientos turista: "))
    cantEconomico = int(input("Asientos económica: "))

    if cantEjecutiva + cantTurista + cantEconomico == 0:
        print("Debe reservar al menos un asiento")
        return


    #------------------RESERVAS YA HECHAS------------------
    totalEjecutiva = 0
    totalTurista = 0
    totalEconomica = 0

    archivo = open("reservas.txt","r")

    for linea in archivo:
        datos = linea.strip().split(";")

        if numeroVuelo.lower() == datos[2].lower():
            totalEjecutiva += int(datos[13])
            totalTurista += int(datos[14])
            totalEconomica += int(datos[15])

    archivo.close()


    #------------------CAPACIDAD DEL AVIÓN------------------
    archivo = open("avionesAerolineas.txt","r")

    marca = ""
    modelo = ""

    for linea in archivo:
        datos = linea.strip().split(";")

        if matricula.lower() == datos[0].lower():
            marca = datos[1]
            modelo = datos[2]

    archivo.close()


    archivo = open("modeloAviones.txt","r")

    capacidadEjecutiva = 0
    capacidadTurista = 0
    capacidadEconomica = 0

    for linea in archivo:
        datos = linea.strip().split(";")

        if modelo.lower() == datos[0].lower() and marca.lower() == datos[1].lower():
            capacidadEjecutiva = int(datos[2])
            capacidadTurista = int(datos[3])
            capacidadEconomica = int(datos[4])

    archivo.close()


    #------------------VALIDAR DISPONIBILIDAD------------------
    if cantEjecutiva > (capacidadEjecutiva - totalEjecutiva):
        print("No hay asientos ejecutiva disponibles")
        return

    if cantTurista > (capacidadTurista - totalTurista):
        print("No hay asientos turista disponibles")
        return

    if cantEconomico > (capacidadEconomica - totalEconomica):
        print("No hay asientos económica disponibles")
        return


    #------------------MONTO TOTAL------------------
    montoTotal = (cantEjecutiva * montoEjecutiva) + (cantTurista * montoTurista) + (cantEconomico * montoEconomico)


    #------------------FECHA Y HORA RESERVACIÓN------------------
    fechaReserva = input("Fecha reservación (dd/mm/aaaa): ")
    horaReserva = input("Hora reservación: ")

    idReserva = generarIdReservacion()


    #------------------GUARDAR------------------
    archivo = open("reservas.txt","a")

    archivo.write(
        idReserva+";"+nombre+";"+numeroVuelo+";"+fechaReserva+";"+horaReserva+";"+ aerolinea+";"+matricula+";"+
        codigoSalida+";"+fechaSalida+";"+horaSalida+";"+ codigoLlegada+";"+fechaLlegada+";"+horaLlegada+";"+ str(cantEjecutiva)+";"+str(cantTurista)+";"+str(cantEconomico)+";"+
        str(montoTotal)+"\n"
    )

    archivo.close()


    #------------------COMPROBANTE------------------
    print("\n--- COMPROBANTE ---")
    print("Identificador de reserva:", idReserva)
    print("Nombre:", nombre)

    print("Fecha reservación:", fechaReserva)
    print("Hora reservación:", horaReserva)

    print("Vuelo:", numeroVuelo)
    print("Aerolínea:", aerolinea)
    print("Avión:", matricula)

    print("Salida:", codigoSalida, fechaSalida, horaSalida)
    print("Llegada:", codigoLlegada, fechaLlegada, horaLlegada)

    print("Ejecutiva:", cantEjecutiva)
    print("Turista:", cantTurista)
    print("Económica:", cantEconomico)

    print("Total:", montoTotal)

#------------Cancelación de reservación----------------------
"""
Nombre: cancelarReservacion
Entrada: No tiene
Salida: Elimina una reservación del sistema si el usuario confirma la acción
Restricciones:
    - El archivo "reservas.txt" debe existir
    - El identificador debe existir dentro del archivo para poder eliminarse
    - El usuario debe confirmar con "sí" para proceder con la cancelación
"""
def cancelarReservacion():

    idEliminar = input("Ingrese el ID de la reservación a cancelar: ")

    archivo = open("reservas.txt","r")
    lineas = archivo.readlines()
    archivo.close()

    existe = False

    #------------------VALIDAR EXISTENCIA------------------
    for linea in lineas:

        if linea.strip() != "":

            datos = linea.strip().split(";")

            if idEliminar.lower() == datos[0].lower():
                existe = True

                print("\n--- RESERVACIÓN ENCONTRADA ---")
                print("ID:", datos[0])
                print("Nombre:", datos[1])
                print("Vuelo:", datos[2])
                print("Fecha reservación:", datos[3])
                print("Hora reservación:", datos[4])

    if not existe:
        print("La reservación no existe")
        return


    confirmar = input("¿Desea cancelar esta reservación? (si/no): ")

    if confirmar.lower() != "si":
        print("Cancelación cancelada")
        return


    #------------------ELIMINAR------------------
    archivo = open("reservas.txt","w")

    for linea in lineas:

        if linea.strip() != "":

            datos = linea.strip().split(";")

            if idEliminar.lower() != datos[0].lower():
                archivo.write(linea)
        else:
            archivo.write(linea)

    archivo.close()

    print("Reservación cancelada correctamente")

# ---------------- EJECUCIÓN ----------------
menuPrincipal()
