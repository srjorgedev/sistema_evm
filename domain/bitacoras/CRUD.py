from db.ConnB import Conn
from domain.bitacoras.Clase import Bitacora
from mysql.connector import Error

def listaGeneral() -> list[tuple]:
    conn = Conn()

    query = """
        SELECT 
            numero as id,
            asunto,
            destino, 
            entrada, 
            salida
        FROM bitacora
        WHERE visible = FALSE
    """
    
    # print("CRUD.listaGeneral ejecutándose...")
    lista = conn.lista(query)

    # print("CRUD LISTA EJECUTADO")

    bitacoras = []
    for fila in lista:
        id, asunto, destino, entrada, salida = fila
        
        bitacora = (id, asunto, destino, entrada, salida)

        bitacoras.append(bitacora)

    return bitacoras

def listaArchivados() -> list[Bitacora]:
    conn = Conn()

    query = """
        SELECT 
            numero as id,
            asunto,
            destino, 
            entrada, 
            salida
        FROM bitacora
        WHERE visible = FALSE
    """
    
    # print("CRUD.listaGeneral ejecutándose...")
    lista = conn.lista(query)

    # print("CRUD LISTA EJECUTADO")

    bitacoras = []
    for fila in lista:
        id, asunto, destino, entrada, salida = fila
        
        listaItem = Bitacora()
        listaItem.set_numControl(id)
        listaItem.set_asunto(asunto)
        listaItem.set_destino(destino)
        listaItem.set_entradaBool(entrada)
        listaItem.set_salidaBool(salida)

        bitacoras.append(listaItem)

    return bitacoras

def archivar(data: int):
    conn = Conn()
    
    query = """
        UPDATE bitacora 
        SET visible = FALSE
        WHERE numero = %s
    """
    
    params = (data,)
    
    r = conn.actualizar(query, params)
    
    return r

def bitacoraSinEntrada():
    conn = Conn()

    query = 'SELECT numControl as "Numero de control", asunto as Asunto, destino as Destino, salida as Salida, entrada as Entrada '
    query += 'FROM bitacora WHERE entrada IS NULL AND status = 1'
    lista = conn.lista(query)

    if lista == 0 or len(lista) == 0:
        print("   No se puede mostrar.")
        return

    for fila in lista:
        numCtrl, asunto, destino, salida, entrada = fila
        if entrada == None: entrada = 0

        print(f"{numCtrl:<8}{asunto:<35}{destino:<15}{salida:<12}{entrada}")

    return len(lista)


def existe(bitacora: Bitacora):
    conn = Conn()

    aux = "SELECT asunto, destino, responsable, autorizador, vehiculo, gasSalida, kmSalida, fechaSalida FROM bitacora WHERE numControl = {0}"
    query = aux.format(bitacora.get_numControl())

    lista = conn.lista(query)

    return lista


def crearSalida(bitacora: Bitacora):
    conn = Conn()

    aux = "INSERT INTO bitacora (asunto, destino, responsable, autorizador, vehiculo, gasSalida, kmSalida, fechaSalida) "
    aux += "VALUES ('{0}', '{1}', {2}, {3}, '{4}', '{5}', '{6}', '{7}')"

    query = aux.format(bitacora.get_asunto(), bitacora.get_destino(),
                       bitacora.get_responsable(), bitacora.get_autorizador(),
                       bitacora.get_vehiculo(),
                       bitacora.get_salida().get_gasolina(),
                       bitacora.get_salida().get_kilometraje(),
                       bitacora.get_salida().get_fecha())

    return conn.registrar(query)


def crearEntrada(bitacora: Bitacora):
    conn = Conn()

    aux = "UPDATE bitacora SET gasEntrada = '{0}', kmEntrada = '{1}', fechaEntrada = '{2}', entrada = 1, "
    aux += "totalKM = {3}, kmPorLitro = {4}, gasConsumida = {5}"
    aux += "WHERE numControl = {6}"

    query = aux.format(bitacora.get_entrada().get_gasolina(),
                       bitacora.get_entrada().get_kilometraje(),
                       bitacora.get_entrada().get_fecha(),
                       bitacora.get_kilometrajeTotal(),
                       bitacora.get_gasolinaRendimiento(),
                       bitacora.get_gasolinaConsumida(),
                       bitacora.get_numControl())

    return conn.registrar(query)


def baja(bitacora: Bitacora):
    conn = Conn()

    aux = "UPDATE bitacora SET status = 0 "
    aux += "WHERE numControl = {0}"

    query = aux.format(bitacora.get_numControl())

    return conn.actualizar(query)


def actualizarDestino(bitacora: Bitacora):
    conn = Conn()

    aux = "UPDATE bitacora SET destino = '{0}' "
    aux += "WHERE numControl = {1}"

    query = aux.format(bitacora.get_destino(), bitacora.get_numControl())

    return conn.actualizar(query)
