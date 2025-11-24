from db.ConnB import Conn
from mysql.connector import Error

from utils.log import log

def lista_tipos_observacion(): 
    conn = Conn()
    
    query = """
    SELECT 
        codigo,
        descripcion
    FROM tipo_observacion
    """
    
    lista = conn.lista(query)
    
    tipos = []
    for tupla in lista:
        tipos.append((tupla[0], tupla[1]))
    
    return tipos