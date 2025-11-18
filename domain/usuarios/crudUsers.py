from db.connU import conn
from domain.usuarios.ClaseUsuarios import Usuario, TipoEmpleado

#Create
#Read
#Update
#Delete
#Buscar
'''
#def __init__(self, numEmpleado, nombre, tipo_empleado, activo):
def __init__(self, codigo, descripcion):
)
'''


#Create insert
def Create(newUser, newTipo):
    objUser = Usuario(0, "", "", 0)
    objUser = newUser
    objTipo = TipoEmpleado
    objTipo = newTipo
    miConn = conn()
    aux2 = "INSERT INTO tipo_empleado(codigo, descripcion) VALUES ('{0}','{1}')"
    comando2 = aux2.format(objTipo.get_codigo(), objTipo.get_descripcion())
    miConn.register2(comando2)
    aux = "INSERT INTO empleado(nombre, tipo_empleado, activo) VALUES ('{0}','{1}','{2}')"
    comando = aux.format(objUser.get_nombre(), objTipo.get_codigo(), objUser.get_activo())
    miConn.register(comando)



#Read select
def Select():
    miConn = conn()
    comando = "select * from usuario"
    listado = miConn.lista(comando)

    if listado == 0:
        print("   No se puede mostrar")
    else:
        if len(listado) > 0:
            for fila in listado:
                objUser = Usuario(fila[0], fila[1], fila[2], fila[3], fila[4],
                                  fila[5], fila[6])
                print(objUser)
                print()


def selectInd(oldUser):
    objUser = Usuario("", "", "", "", "", 0, "")
    objUser = oldUser
    miConn = conn()
    aux = "select * from usuario where numEmpleado = {0}"
    comando = aux.format(objUser.get_numEmpleado())
    listado = miConn.lista(comando)
    if len(listado) == 1:
        print("   Datos de Usuario:")
        print()
        for fila in listado:
            obj = Usuario(
                fila[0],  # customerID
                fila[1],  # storeID
                fila[2],  # first_name
                fila[3],  # last_name
                fila[4],  # email
                fila[5],  # addressID
                fila[6])
            print(obj)

        return True
    else:
        return False


#Update
def UpdateNombre(oldUser):
    objUser = Usuario("", "", "", "", "", 0, "")
    objUser = oldUser
    miConn = conn()
    aux = "UPDATE usuario SET nombre = '{0}' WHERE numEmpleado = {1}"
    comando = aux.format(objUser.get_nombre(), objUser.get_numEmpleado())
    miConn.actualizar(comando)


def UpdateTelefono(oldUser):
    objUser = Usuario("", "", "", "", "", 0, "")
    objUser = oldUser
    miConn = conn()
    aux = "UPDATE usuario SET telefono = '{0}' WHERE numEmpleado = {1}"
    comando = aux.format(objUser.get_telefono(), objUser.get_numEmpleado())
    miConn.actualizar(comando)


def UpdateTipoEmpleado(oldUser):
    objUser = Usuario("", "", "", "", "", 0, "")
    objUser = oldUser
    miConn = conn()
    aux = "UPDATE usuario SET tipoEmpleado = '{0}' WHERE numEmpleado = {1}"
    comando = aux.format(objUser.get_tipoEmpleado(), objUser.get_numEmpleado())
    miConn.actualizar(comando)


#Delete
def Delete(oldUser):
    objUser = Usuario("", "", "", "", "", 0, "")
    objUser = oldUser
    miConn = conn()
    aux = "UPDATE usuario SET activo = {0} WHERE numEmpleado = {1}"
    comando = aux.format(objUser.get_activo(), objUser.get_numEmpleado())
    miConn.actualizar(comando)


    #Buscar
def Deactive(oldUser):
    objUser = Usuario("", "", "", "", "", 0, "")
    objUser = oldUser
    miConn = conn()
    aux = "select * from usuario where numEmpleado = {0}"
    comando = aux.format(objUser.get_numEmpleado())
    listado = miConn.lista(comando)
    if len(listado) == 1:
        print("   Datos a Inhabilitar: ")
        for fila in listado:
            obj = Usuario(
                fila[0],  # customerID
                fila[1],  # storeID
                fila[2],  # first_name
                fila[3],  # last_name
                fila[4],  # email
                fila[5],  # addressID
                fila[6])
            print(obj)
        return True
    else:
        return False


#Buscar
def buscar(oldUser):
    objUser = Usuario("", "", "", "", "", 0, "")
    objUser = oldUser
    miConn = conn()
    aux = "select * from usuario where numEmpleado = {0}"
    comando = aux.format(objUser.get_numEmpleado())
    listado = miConn.lista(comando)
    if len(listado) == 1:
        print("   Datos a modificar: ")
        for fila in listado:
            obj = Usuario(
                fila[0],  # customerID
                fila[1],  # storeID
                fila[2],  # first_name
                fila[3],  # last_name
                fila[4],  # email
                fila[5],  # addressID
                fila[6])
            print(obj)
        return True
    else:
        return False
