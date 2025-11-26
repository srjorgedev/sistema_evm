import domain.usuarios.CRUD as CRUD

def lista_general():
    return CRUD.lista_general()

def lista_tipos():
    return CRUD.lista_tipos()

def lista_choferes():
    return CRUD.lista_choferes()

def registrar_general(data: dict):
    return CRUD.registrar_empleado(data)

def lista_contactos():
    return CRUD.lista_contactos()