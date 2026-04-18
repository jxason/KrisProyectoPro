# ============================ MENÚ PRINCIPAL ============================

"""
Nombre: 
Entradas: 
Salidas:
Restricciones:
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


# ------------------------------- ACCESO CLAVE ----------------------

"""
Nombre: 
Entradas: 
Salidas:
Restricciones:
"""
def accesoAdministrativo():
    clave = input("Ingrese la clave de acceso: ")

    if claveValida(clave):
        menuAdministrativo()
    else:
        print("Clave Incorrecta")


"""
Nombre: 
Entradas: 
Salidas:
Restricciones:
"""
def leerClaveAcceso():
    archivo = open("acceso.txt","r")
    clave = archivo.read().strip()
    archivo.close()
    return clave


"""
Nombre: 
Entradas: 
Salidas:
Restricciones:
"""
def claveValida(claveIngresada):
    archivo = open("acceso.txt","r")

    for linea in archivo:
        linea = linea.strip()

        if claveIngresada == linea:
            archivo.close()
            return True

    archivo.close()
    return False


# ---------------------------- MENÚS ------------------------------

"""
Nombre: 
Entradas: 
Salidas:
Restricciones:
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
            print("Gestión de vuelos (pendiente)")
        elif opcion == "6":
            print("Historial de reservaciones (pendiente)")
        elif opcion == "7":
            print("Estadísticas (pendiente)")
        elif opcion == "8":
            print("Regresando al menú principal...")
            break
        else:
            print("Opción inválida")


"""
Nombre: 
Entradas: 
Salidas:
Restricciones:
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
            print("(pendiente)")
        elif opcion == "2":
            print(" (pendiente)")
        elif opcion == "3":
            print("(pendiente)")
        elif opcion == "4":
            print("Regresando al Menú Principal...")
            break
        else:
            print("Opción invalida")


# ---------------------- SUBMENÚS ------------------------

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
            print("Regresando al Menú Administrativo...")
            break
        else:
            print("Opción invalida")


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
            print("Regresando al Menú Administrativo...")
            break
        else:
            print("Opción inválida")


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
            print("Regresando al Menu Administrativo...")
            break
        else:
            print("Opción inválida")


def menuGestionDeAvionesAerolinea():
    while True:
        print("\n ---MENÚ GESTIÓN DE AEROLÍNEAS---")
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
            print("Regresando al Menu Administrativo...")
            break
        else:
            print("Opción inválida")


# --------------------------------- GESTIÓN MARCAS ----------------------

def mostrarMarcas():
    archivo = open("aviones.txt","r")

    print("\n--- LISTA DE MARCAS ---")
    for linea in archivo:
        print(linea.strip())

    archivo.close()


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


def eliminarMarca():
    eliminarMarca = input("Ingrese la marca a eliminar: ")

    archivo = open("modeloAviones.txt","r")
    for linea in archivo:
        datos = linea.strip().split(";")

        if eliminarMarca.lower() == datos[1].lower():
            print("No se puede eliminar, la marca está asociada a un modelo")
            archivo.close()
            return
    archivo.close()

    archivo = open("aviones.txt","r")
    contenidoLineas = archivo.readlines()
    archivo.close()

    archivo = open("aviones.txt","w")

    for linea in contenidoLineas:
        if eliminarMarca.lower() != linea.strip().lower():
            archivo.write(linea)

    archivo.close()
    print("Marca eliminada")
    
# ---------------------- GESTIÓN MODELOS --------------------------

def mostrarModelos():
    archivo = open("modeloAviones.txt","r")

    print("\n--- LISTA DE MODELOS ---")
    for linea in archivo:
        print(linea.strip())

    archivo.close()


def incluirModelo():
    modelo = input("Descripción del modelo: ")
    marca = input("Marca: ")
    ejecutiva = input("Asientos ejecutivos: ")
    turista = input("Asientos turistas: ")
    economico = input("Asientos económicos: ")

    archivo = open("modeloAviones.txt","r")
    for linea in archivo:
        if modelo.lower() == linea.split(";")[0].lower():
            print("Ese modelo ya existe")
            archivo.close()
            return
    archivo.close()

    archivo = open("aviones.txt","r")
    existe = False
    for linea in archivo:
        if marca.lower() == linea.strip().lower():
            existe = True
    archivo.close()

    if not existe:
        print("La marca no existe")
        return

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
            marca = input("Nueva marca: ")
            ejecutiva = input("Asientos Ejecutivos: ")
            turista = input("Asientos Turista: ")
            economico = input("Asientos Económicos: ")

            archivo.write(modelo+";"+marca+";"+ejecutiva+";"+turista+";"+economico)
        else:
            archivo.write(linea)

    archivo.close()

    if encontrado:
        print("Modelo modificado")
    else:
        print("Ese modelo no existe")


def eliminarModelo():
    eliminarModelo = input("Ingrese el modelo a eliminar: ")

    archivo = open("modeloAviones.txt","r")
    contenidoLineas = archivo.readlines()
    archivo.close()

    archivo = open("modeloAviones.txt","w")

    for linea in contenidoLineas:
        if eliminarModelo.lower() != linea.split(";")[0].lower():
            archivo.write(linea)

    archivo.close()
    print("Modelo eliminado")



# ---------------------------- GESTIÓN DE AVIONES POR AEROLÍNEAS ----------------

def mostrarAerolineas():
    archivo = open("aerolineas.txt","r")

    print("\n--- LISTA DE AEROLÍNEAS ---")
    for linea in archivo:
        print(linea.strip())

    archivo.close()


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


def eliminarAerolinea():
    eliminar = input("Ingrese la aerolínea a eliminar: ")

    archivo = open("aerolineas.txt","r")
    contenidoLineas = archivo.readlines()
    archivo.close()

    existe = False

    for linea in contenidoLineas:
        datos = linea.strip().split(";")

        if eliminar.lower() == datos[0].lower():
            existe = True

    if not existe:
        print("La aerolínea no existe, no puede ser eliminada")
        return

    archivo = open("aerolineas.txt","w")

    for linea in contenidoLineas:
        datos = linea.strip().split(";")

        if eliminar.lower() != datos[0].lower():
            archivo.write(linea)

    archivo.close()
    print("Aerolínea eliminada")

   
# ------------------------ GESTIÓN AEROLÍNEAS (VERSIÓN 2 - DUPLICADA) -------------------

def mostrarAerolineas():
    archivo = open("aerolineas.txt","r")

    print("\n--- LISTA DE AEROLÍNEAS ---")
    for linea in archivo:
        print(linea.strip())

    archivo.close()


def incluirAerolinea():
    nombreAerolinea = input("Nombre de la aerolínea: ")
    centroOperaciones = input("Centro de operaciones: ")

    archivo = open("aerolineas.txt","r")

    for linea in archivo:
        datos = linea.strip().split(";")

        if nombreAerolinea.lower() == datos[0].lower():
            print("Esa aerolínea ya existe")
            archivo.close()
            return

    archivo.close()

    archivo = open("aerolineas.txt","a")
    archivo.write("\n"+nombreAerolinea+";"+centroOperaciones)
    archivo.close()

    print("Aerolínea agregada")


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

            archivo.write("\n"+nombre+";"+centro)
        else:
            archivo.write(linea)

    archivo.close()

    if encontrado:
        print("Aerolínea modificada")
    else:
        print("Esa aerolínea no existe")


def eliminarAerolinea():
    eliminar = input("Ingrese la aerolínea a eliminar: ")

    archivo = open("aerolineas.txt","r")
    contenidoLineas = archivo.readlines()
    archivo.close()

    existe = False

    for linea in contenidoLineas:
        datos = linea.strip().split(";")

        if eliminar.lower() == datos[0].lower():
            existe = True

    if not existe:
        print("La aerolínea no existe, no puede ser eliminada")
        return

    archivo = open("aerolineas.txt","w")

    for linea in contenidoLineas:
        datos = linea.strip().split(";")

        if eliminar.lower() != datos[0].lower():
            archivo.write(linea)

    archivo.close()
    print("Aerolínea eliminada")


# ---------------------------- AVIONES POR AEROLÍNEA ------------------------------

def mostrarAviones():
    archivo = open("avionesAerolineas.txt","r")

    print("\n--- LISTA DE AVIONES --")
    for linea in archivo:
        print(linea.strip())

    archivo.close()


def incluirAvion():
    matricula = input("Matrícula: ")

    archivo = open("avionesAerolineas.txt","r")
    for linea in archivo:
        datos = linea.strip().split(";")
        if matricula.lower() == datos[0].lower():
            print("Esa matrícula ya existe")
            archivo.close()
            return
    archivo.close()

    print("\nMarcas disponibles:")
    archivo = open("aviones.txt","r")
    for linea in archivo:
        print(linea.strip())
    archivo.close()

    marca = input("Seleccione una marca: ")

    archivo = open("aviones.txt","r")
    existeMarca = False
    for linea in archivo:
        if marca.lower() == linea.strip().lower():
            existeMarca = True
    archivo.close()

    if not existeMarca:
        print("La marca no existe")
        return

    print("\nModelos disponibles para esa marca:")
    archivo = open("modeloAviones.txt","r")

    for linea in archivo:
        datos = linea.strip().split(";")

        if marca.lower() == datos[1].strip().lower():
            print(datos[0])

    archivo.close()

    modelo = input("Seleccione un modelo: ")

    archivo = open("modeloAviones.txt","r")
    existeModelo = False
    for linea in archivo:
        datos = linea.strip().split(";")

        if modelo.lower() == datos[0].strip().lower() and marca.lower() == datos[1].strip().lower():
            existeModelo = True
    archivo.close()

    if not existeModelo:
        print("El modelo no existe para esa marca")
        return

    anio = input("Año: ")

    print("\nAerolíneas disponibles:")
    archivo = open("aerolineas.txt","r")
    for linea in archivo:
        datos = linea.strip().split(";")
        print(datos[0])
    archivo.close()

    aerolinea = input("Seleccione una aerolínea: ")

    archivo = open("aerolineas.txt","r")
    existeAerolinea = False
    for linea in archivo:
        datos = linea.strip().split(";")

        if aerolinea.lower() == datos[0].lower():
            existeAerolinea = True
    archivo.close()

    if not existeAerolinea:
        print("La aerolínea no existe")
        return

    archivo = open("avionesAerolineas.txt","a")
    archivo.write("\n"+matricula+";"+marca+";"+modelo+";"+anio+";"+aerolinea)
    archivo.close()

    print("Avión agregado")


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


def eliminarAvion():
    eliminar = input("Ingrese la matrícula del avión a eliminar: ")

    archivo = open("avionesAerolineas.txt","r")
    contenidoLineas = archivo.readlines()
    archivo.close()

    existe = False

    for linea in contenidoLineas:
        datos = linea.strip().split(";")

        if eliminar.lower() == datos[0].lower():
            existe = True

    if not existe:
        print("El avión no existe, no puede ser eliminado")
        return

    archivo = open("avionesAerolineas.txt","w")

    for linea in contenidoLineas:
        datos = linea.strip().split(";")

        if eliminar.lower() != datos[0].lower():
            archivo.write(linea)

    archivo.close()
    print("Avión eliminado")

# ------------------------ EJECUCIÓN ----------------------

menuPrincipal()
