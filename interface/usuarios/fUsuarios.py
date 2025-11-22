from domain.usuarios.ClaseUsuarios import Usuario, TipoEmpleado, Telefono, Licencia, TipoLicencia
import domain.usuarios.crudUsers as crudUsers
from interface.usuarios.Menu import _Tipos
from interface.usuarios.Menu import licencias
from interface.usuarios.Menu import datos
from interface.usuarios import val
import random
import bcrypt

'''
////Codigo verificacion de hash de password
entered_password = input("Contraseña: ").encode('utf-8')
stored_hash = resultado_sql[0]["password_hash"].encode('utf-8')

if bcrypt.checkpw(entered_password, stored_hash):
    print("Login correcto")
else:
    print("Contraseña incorrecta")

 #000
 if bcrypt.checkpw(passwordIngresada.encode('utf-8'), hash_guardado):
    print("Correcto")
else:
    print("Incorrecto")

    '''
'''
def __init__(self, numEmpleado, nombre, activo):
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
            codigo = str(random.randint(10000, 99999))
            descripcion = "Administrador"
            while True:
                password = input("Cree una contraseña: ")
                if val.validate_password(password):
                    password = password.encode('utf-8')
                    hashed = bcrypt.hashpw(password, bcrypt.gensalt())
                    print("Contraseña Valida")
                    break
                else:
                    print("Contraseña Invalida. Intente de nuevo")
                    print("La contraseña debe cumplir con los siguientes requisitos para ser válida:")
                    print(" 1. Tener al menos 8 caracteres.")
                    print(" 2. Incluir al menos una letra mayúscula (A-Z).")
                    print(" 3. Incluir al menos una letra minúscula (a-z).")
                    print(" 4. Incluir al menos un número (0-9).")
            email = val.vEmail("Ingrese su Correo Electronico: ")
            newTipo = TipoEmpleado(codigo, descripcion)
            newUser = Usuario(None, nombre, newTipo.get_codigo(), 1, hashed, email)
            newTel = Telefono(None, telefono ,None)
            crudUsers.Create(newUser, newTipo, newTel)
        case 2:
            codigo = str(random.randint(10000, 99999))
            descripcion = "Chofer"
            licencias()
            opclicencia = int(input("   Ingrese una opcion: "))
            match opclicencia:
                case 1:
                    codigoLic = "A"
                    print("    Eligio la opcion de licencia " + codigoLic + ".")
                    descripcionLic = "Automovilista"
                case 2:
                    codigoLic = "B"
                    print("    Eligio la opcion de licencia " + codigoLic + ".")
                    descripcionLic = "Taxis y Aplicaciones"
                case 3:
                    codigoLic = "C"
                    print("    Eligio la opcion de licencia " + codigoLic + ".")
                    descripcionLic = "Transporte público"
                case 4:
                    codigoLic = "D"
                    print("    Eligio la opcion de licencia " + codigoLic + ".")
                    descripcionLic = "Transporte de carga"
                case 5:
                    codigoLic = "E"
                    print("    Eligio la opcion de licencia " + codigoLic + ".")
                    descripcionLic = "Servicios especializados  y carga"
            print()
            while True:
                numeroLicencia = input("   Ingrese su numero de licencia: ")
                if val.valLicencia(numeroLicencia):
                    print("    Número de licencia válido.")
                    break
                else:
                    print(
                        "    Número de licencia inválido. Debe comenzar con una letra mayuscula y tener 9 o 10 dígitos."
                    )
            exp = val.val_exp()
            ven = val.val_ven(exp)
            while True:
                password = input("Cree una contraseña: ")
                if val.validate_password(password):
                    password = password.encode('utf-8')
                    hashed = bcrypt.hashpw(password, bcrypt.gensalt())
                    print("Contraseña Valida")
                    break
                else:
                    print("Contraseña Invalida. Intente de nuevo")
                    print("La contraseña debe cumplir con los siguientes requisitos para ser válida:")
                    print(" 1. Tener al menos 8 caracteres.")
                    print(" 2. Incluir al menos una letra mayúscula (A-Z).")
                    print(" 3. Incluir al menos una letra minúscula (a-z).")
                    print(" 4. Incluir al menos un número (0-9).")
            email = val.vEmail("Ingrese su Correo Electronico: ")
            newTipo = TipoEmpleado(codigo, descripcion)
            newUser = Usuario(None, nombre, newTipo.get_codigo(), 1, hashed, email)
            newTel = Telefono(None, telefono ,None)
            newTLic = TipoLicencia(codigoLic, descripcionLic)
            newLic = Licencia(numeroLicencia, exp, ven, None, newTLic.get_codigoLic())
            crudUsers.Create(newUser, newTipo, newTel, newTLic, newLic)
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
