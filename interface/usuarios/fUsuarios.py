from domain.usuarios.ClaseUsuarios import Usuario
import domain.usuarios.crudUsers as crudUsers
from interface.usuarios.Menu import _Tipos
from interface.usuarios.Menu import licencias
from interface.usuarios.Menu import datos
from interface.usuarios import val
'''
create table usuario(
    nombre varchar(15) not null,
    telefono varchar(10) not null unique,
    tipoEmpleado varchar(10) not null,
    licencia varchar(15),
    numeroLicencia varchar(20) unique,
    numEmpleado int not null auto_increment primary key
)
'''


def createUser():
    print("    --REGISTRAR USUARIO--")
    while True:
        nombrePila = input("   Ingrese su nombre(s): ")
        if val.vNombre(nombrePila):
            print("Nombre válido:", nombrePila)
            break
        else:
            print(
                "   Nombre inválido. Solo se permiten letras y espacios (sin números ni símbolos)."
            )
            print("   Por favor, intente de nuevo.\n")
    while True:
        apellidos = input("   Ingrese su(s) apellido(s): ")
        if val.vNombre(apellidos):
            print("Apellido(s) válido(s):", apellidos)
            break
        else:
            print(
                "   Nombre inválido. Solo se permiten letras y espacios (sin números ni símbolos)."
            )
            print("   Por favor, intente de nuevo.\n")
    nombre = nombrePila + " " + apellidos
    print("Nombre: " + nombre)
    print()
    telefono = val.valTelefono()
    _Tipos()
    opcEmpleado = val.vInt("Seleccion el tipo de empleado:  ")
    match opcEmpleado:
        case 1:
            tipoEmpleado = "Administrador"
            newUser = Usuario(nombre, telefono, tipoEmpleado, None, None, None,
                              None)
            crudUsers.Create(newUser)
        case 2:
            tipoEmpleado = "Chofer"
            licencias()
            opclicencia = int(input("   Ingrese una opcion: "))
            match opclicencia:
                case 1:
                    licencia = "Tipo A"
                    print("    Eligio la opcion de licencia " + licencia + ".")
                case 2:
                    licencia = "Tipo B"
                    print("    Eligio la opcion de licencia " + licencia + ".")
                case 3:
                    licencia = "Tipo C"
                    print("    Eligio la opcion de licencia " + licencia + ".")
                case 4:
                    licencia = "Tipo D"
                    print("    Eligio la opcion de licencia " + licencia + ".")
                case 5:
                    licencia = "Tipo E"
                    print("    Eligio la opcion de licencia " + licencia + ".")
            print()
            numeroLicencia = input("   Ingrese su numero de licencia: ")
            while True:
                if val.valLicencia(numeroLicencia):
                    print("    Número de licencia válido.")
                    break
                else:
                    print(
                        "    Número de licencia inválido. Debe comenzar con una letra y tener 9 o 10 dígitos."
                    )
                    numeroLicencia = input(
                        "   Ingrese su numero de licencia: ")
            newUser = Usuario(nombre, telefono, tipoEmpleado, licencia,
                              numeroLicencia, None, None)
            crudUsers.Create(newUser)
        case 3:
            tipoEmpleado = "Vigilante"
            newUser = Usuario(nombre, telefono, tipoEmpleado, None, None, None,
                              None)
            crudUsers.Create(newUser)
        case 4:
            tipoEmpleado = "Usuario"
            newUser = Usuario(nombre, telefono, tipoEmpleado, None, None, None,
                              None)
            crudUsers.Create(newUser)


def selectUser():
    print("   Listado de Usuarios: ")
    print()
    crudUsers.Select()
    numEmpleado = val.vInt("Ingrese el numero de Empeleado del empleado: ")
    oldUser = Usuario("", "", "", "", "", numEmpleado, "")
    crudUsers.selectInd(oldUser)


def updateUser():
    print("   Actualizar Usuario: ")
    numEmpleado = val.vInt(
        "Ingrese el numero de Empeleado del empleado que desea modificar: ")
    oldUser = Usuario("", "", "", "", "", numEmpleado, "")
    crudUsers.buscar(oldUser)
    datos()
    opcMod = int(
        input("   Seleccione el dato del usuario que desea modificar: "))
    match opcMod:
        case 1:
            nombrePila = val.vTexto("Ingrese su nombre(s) de pila: ")
            primerApell = val.vTexto("Ingrese su primer apellido: ")
            segundoApell = val.vTexto(
                "En caso de contar con uno, ingrese su segundo apellido, si no, de ENTER: "
            )
            nombre = nombrePila + " " + primerApell + " " + segundoApell
            oldUser.set_nombre(nombre)
            crudUsers.UpdateNombre(oldUser)
        case 2:
            telefono = val.valTelefono()
            oldUser.set_telefono(telefono)
            crudUsers.UpdateTelefono(oldUser)
        case 3:
            _Tipos()
            opcEmpleado = val.vInt("Seleccion el nuevo tipo de empleado:  ")
            match opcEmpleado:
                case 1:
                    tipoEmpleado = "Administrador"
                    oldUser.set_tipoEmpleado(tipoEmpleado)
                    crudUsers.UpdateTipoEmpleado(oldUser)
                case 2:
                    tipoEmpleado = "Chofer"
                    oldUser.set_tipoEmpleado(tipoEmpleado)
                    crudUsers.UpdateTipoEmpleado(oldUser)
                case 3:
                    tipoEmpleado = "Vigilante"
                    oldUser.set_tipoEmpleado(tipoEmpleado)
                    crudUsers.UpdateTipoEmpleado(oldUser)
                case 4:
                    tipoEmpleado = "Usuario"
                    oldUser.set_tipoEmpleado(tipoEmpleado)
                    crudUsers.UpdateTipoEmpleado(oldUser)


def deleteUser():
    print("   Inhabilitar Customer: ")
    numEmpleado = val.vInt(
        "Ingrese el numero de Empleado del empleado que desea inhabilitar: ")
    oldUser = Usuario("", "", "", "", "", numEmpleado, "")
    crudUsers.Deactive(oldUser)
    activo = 0
    oldUser.set_activo(activo)
    crudUsers.Delete(oldUser)
