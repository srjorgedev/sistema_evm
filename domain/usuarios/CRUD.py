from db.ConnB import Conn

def lista_general():
    conn = Conn()

    query = """
        SELECT
            e.numero,
            CONCAT(e.nombrePila, ' ',  e.apdPaterno, ' ', e.apdMaterno) AS nombre,
            tp.descripcion AS rol,
            tp.codigo as rol_codigo
        FROM empleado AS e
        INNER JOIN tipo_empleado AS tp ON e.tipo_empleado = tp.codigo
        ORDER BY e.numero
    """

    lista = conn.lista(query)

    usuarios = []
    for tupla in lista:
        usuarios.append((tupla[0], tupla[1], tupla[2], tupla[3]))

    return usuarios

def lista_tipos():
    conn = Conn()

    query = """
        SELECT codigo, descripcion
        FROM tipo_empleado
    """

    lista = conn.lista(query)
    
    tipos = []
    for tupla in lista:
        tipos.append((tupla[0], tupla[1]))
        
    return tipos

from db.ConnB import Conn

def lista_choferes():
    conn = ConnB()
    
    query = """
            SELECT
            e.numero as "N°",
            CONCAT(e.nombrePila, ' ', e.apdPaterno, ' ', e.apdMaterno) AS Nombre,
            l.numero as "Numero de licencia", -- "
            tl.codigo AS "Tipo de Licencia",
            l.fechaVencimiento AS "Fecha de Vencimiento"
        FROM empleado AS e
        INNER JOIN tipo_empleado AS te ON e.tipo_empleado = te.codigo
        INNER JOIN licencia AS l ON e.numero = l.empleado
        INNER JOIN tipo_licencia AS tl ON l.tipo_licencia = tl.numero
        WHERE te.descripcion = 'Chofer'
    """
    
    lista = conn.lista(query)
    
    choferes = []
    for tupla in lista:
        choferes.append((tupla[0], tupla[1], tupla[2], tupla[3], tupla[4]))

    return choferes

import sys 

def registrar_empleado(data: dict):
    miConn = Conn()

    comando = """
        INSERT INTO empleado
        (nombrePila, apdPaterno, apdMaterno, tipo_empleado, password_hash, email)
        VALUES (%s, %s, %s, %s, %s, %s)
    """
    
    

    valores = (
        data["nombrePila"],
        data["apdPaterno"],
        data["apdMaterno"],
        data["tipo_empleado"],
        data["password_hash"],
        data["email"]
    )

    miConn.registrar(comando, valores)

    return True



def lista_contactos():
    conn = Conn()
    
    query = """
        SELECT 
            e.numero,
            CONCAT(e.nombrePila, ' ', e.apdPaterno, ' ', e.apdMaterno) as Nombre,
            e.email, 
            t.numTelefono
        FROM empleado as e
        INNER JOIN telefono as t on t.empleado = e.numero
    """
    
    lista = conn.lista(query)
    
    # Retornamos la lista de tuplas
    # Estructura esperada: (Numero, Nombre, Email, Telefono)
    return lista