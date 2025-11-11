from db.connU import conn
from domain.usuarios.ClaseUsuarios import Usuario

#Create
#Read
#Update
#Delete
#Buscar
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


#Create insert
def Create(newUser):
    objUser = Usuario("", "", "", "", "", 0, "")
    objUser = newUser
    miConn = conn()
    aux = "INSERT INTO usuario(nombre, telefono, tipoEmpleado, licencia, numeroLicencia) VALUES ('{0}','{1}','{2}','{3}','{4}')"
    comando = aux.format(objUser.get_nombre(), objUser.get_telefono(),
                         objUser.get_tipoEmpleado(), objUser.get_licencia(),
                         objUser.get_numeroLicencia())
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
