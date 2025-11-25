from db.ConnB import Conn
from domain.bitacoras.Clase import Bitacora
from mysql.connector import Error

from utils.log import log

def listaGeneral() -> list[tuple]:
    conn = Conn()

    query = """
        SELECT 
            numero as id,
            asunto,
            destino, 
            entrada, 
            salida,
            visible
        FROM bitacora
        WHERE visible = TRUE
    """
    
    lista = conn.lista(query)

    bitacoras = []
    for fila in lista:
        id, asunto, destino, entrada, salida, visible = fila
        
        bitacora = (id, asunto, destino, entrada, salida, visible)

        bitacoras.append(bitacora)

    return bitacoras

def listaArchivados() -> list[tuple]:
    conn = Conn()

    query = """
        SELECT 
            numero as id,
            asunto,
            destino, 
            entrada, 
            salida,
            visible
        FROM bitacora
        WHERE visible = FALSE
    """

    lista = conn.lista(query)

    bitacoras = []
    for fila in lista:
        id, asunto, destino, entrada, salida, visible = fila
        
        bitacora = (id, asunto, destino, entrada, salida, visible)

        bitacoras.append(bitacora)

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

def desarchivar(data: int):
    conn = Conn()
    
    query = """
        UPDATE bitacora 
        SET visible = TRUE
        WHERE numero = %s
    """
    
    params = (data,)
    
    r = conn.actualizar(query, params)
    
    return r

def bitacoraSinEntrada():
    conn = Conn()

    query = """
    SELECT 
        numero as id,
        asunto,
        destino, 
        entrada, 
        salida,
        visible
    FROM bitacora
    WHERE visible = TRUE AND
    ENTRADA = FALSE
    """
    
    lista = conn.lista(query)

    bitacoras = []
    for fila in lista:
        id, asunto, destino, entrada, salida, visible = fila
        
        bitacora = (id, asunto, destino, entrada, salida, visible)

        bitacoras.append(bitacora)

    return bitacoras

def leer(id: int):
    conn = Conn()

    aux = """
    SELECT 
        CONCAT(soli.nombrePila, ' ', soli.apdPaterno, ' ', soli.apdMaterno) AS Solicitante,
        CONCAT(aut.nombrePila, ' ', aut.apdPaterno, ' ', aut.apdMaterno) AS Autorizador,
        bit.destino AS Destino,
        bit.asunto AS Asunto,
        DATE_FORMAT(bit.fechaSalida, "%d-%m-%y") AS FechaSalida,
        DATE_FORMAT(bit.horaSalida, "%H:%i") AS HoraSalida,
        bit.kmSalida AS KilometrajeSalida,
        bit.gasSalida AS GasolinaSalida,
        DATE_FORMAT(bit.fechaEntrada, "%d-%m-%Y") AS FechaEntrada,
        DATE_FORMAT(bit.horaEntrada, "%H:%i") AS HoraEntrada,
        bit.kmEntrada AS KilometrajeEntrada,
        bit.gasEntrada AS GasolinaEntrada,
        CONCAT(em.nombrePila, ' ', em.apdPaterno, ' ', em.apdMaterno) AS Empleado,
        vehi.matricula AS Matricula,
        mar.nombre AS Marca,
        mol.nombre AS Modelo
    FROM bitacora AS bit
    INNER JOIN solicitud AS sol ON bit.solicitud = sol.numero
    INNER JOIN empleado AS aut ON sol.autorizador = aut.numero
    INNER JOIN empleado AS soli ON sol.solicitante = soli.numero
    INNER JOIN vehiculo AS vehi ON bit.vehiculo = vehi.numSerie
    LEFT JOIN marca AS mar ON vehi.marca = mar.codigo
    LEFT JOIN modelo AS mol ON vehi.modelo = mol.codigo
    LEFT JOIN empleado_bitacora AS eb ON eb.bitacora = bit.numero
    LEFT JOIN empleado AS em ON eb.empleado = em.numero
    WHERE bit.numero = {0}
    """
    query = aux.format(id)

    lista = conn.lista(query)
    
    return lista


def existe(id: int):
    conn = Conn()

    aux = """
    SELECT 
        CONCAT(soli.nombrePila, ' ', soli.apdPaterno, ' ', soli.apdMaterno) AS Solicitante,
        CONCAT(aut.nombrePila, ' ', aut.apdPaterno, ' ', aut.apdMaterno) AS Autorizador,
        bit.destino AS Destino,
        bit.asunto AS Asunto,
        DATE_FORMAT(bit.fechaSalida, "%d-%m-%Y") AS FechaSalida,
        DATE_FORMAT(bit.horaSalida, "%H:%i") AS HoraSalida,
        bit.kmSalida AS KilometrajeSalida,
        bit.gasSalida AS GasolinaSalida,
        DATE_FORMAT(bit.fechaEntrada, "%d-%m-%Y") AS FechaEntrada,
        DATE_FORMAT(bit.horaEntrada, "%H:%i") AS HoraEntrada,
        bit.kmEntrada AS KilometrajeEntrada,
        bit.gasEntrada AS GasolinaEntrada,
        CONCAT(em.nombrePila, ' ', em.apdPaterno, ' ', em.apdMaterno) AS Empleado,
        vehi.matricula AS Matricula,
        mar.nombre AS Marca,
        mol.nombre AS Modelo
    FROM bitacora AS bit
    INNER JOIN solicitud AS sol ON bit.solicitud = sol.numero
    INNER JOIN empleado AS aut ON sol.autorizador = aut.numero
    INNER JOIN empleado AS soli ON sol.solicitante = soli.numero
    INNER JOIN vehiculo AS vehi ON bit.vehiculo = vehi.numSerie
    LEFT JOIN marca AS mar ON vehi.marca = mar.codigo
    LEFT JOIN modelo AS mol ON vehi.modelo = mol.codigo
    LEFT JOIN empleado_bitacora AS eb ON eb.bitacora = bit.numero
    LEFT JOIN empleado AS em ON eb.empleado = em.numero
    WHERE bit.numero = {0}
    """
    query = aux.format(id)

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
