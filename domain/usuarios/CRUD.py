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