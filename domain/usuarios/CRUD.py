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

    lista = conn.lista(query)
    
    tipos = []
    for tupla in lista:
        tipos.append((tupla[0], tupla[1]))
        
    return tipos

from db.ConnB import Conn

def lista_choferes():
    conn = Conn()
    
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


# Continúa en CRUD.py (después de lista_choferes)

# Asegúrate de que la clase Conn esté importada al inicio: from db.ConnB import Conn

def registrar_general(user_data: dict):
    conn = Conn()

    # --- 1. Insertar Empleado (nombrePila, apdPaterno, apdMaterno, tipo_empleado) ---
    query_empleado = """
        INSERT INTO empleado (nombrePila, apdPaterno, apdMaterno, tipo_empleado)
        VALUES (%s, %s, %s, %s)
    """
    params_empleado = (
        user_data['nombrePila'],
        user_data['apdPaterno'],
        user_data['apdMaterno'],
        user_data['tipo_empleado']
    )

    # Ejecutar la inserción y obtener el ID del nuevo empleado (e.numero)
    # **IMPORTANTE:** Esto asume que tu objeto Conn tiene un método que devuelve el último ID insertado.
    # Si no tienes ese método, tendrás que usar una consulta SELECT LAST_INSERT_ID() después de ejecutar_commit.
    try:
        # Usando el método que devuelve el ID:
        empleado_id = conn.ejecutar_commit_and_return_id(query_empleado, params_empleado) 
    except AttributeError:
        # Si conn.ejecutar_commit_and_return_id no existe, usa la que sí tienes:
        conn.ejecutar_commit(query_empleado, params_empleado)
        empleado_id = conn.get_last_insert_id() # Asumiendo que existe un método para obtener el ID

    if empleado_id:
        # --- 2. Insertar Credenciales (correo, contrasena, empleado_numero) ---
        query_login = """
            INSERT INTO login (correo, contrasena, empleado_numero)
            VALUES (%s, %s, %s)
        """
        params_login = (
            user_data['correo'], 
            user_data['contrasena'], 
            empleado_id # Usamos el ID del empleado
        )
        
        conn.ejecutar_commit(query_login, params_login)
        
        return f"Registro exitoso. Empleado N° {empleado_id}"
        
    else:
        return "Error: No se pudo obtener el ID del nuevo empleado para registrar el login."
    

# En domain/usuarios/CRUD.py

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