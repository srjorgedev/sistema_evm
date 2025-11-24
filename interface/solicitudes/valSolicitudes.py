import datetime
def vOpciones(msg,inf,sup, funcion):
    while True:
        funcion()
        valor=input(msg)
        if valor.isdigit() != True:
            print("Solo ingresa números enteros")
        else:
            valor = int(valor)
            if (valor>=inf and valor<=sup):
                return valor
            else:
                print("Esta fuera de rango")
                
def vAsunto(msg):
    while True:
        valor=input(msg)
        if len(valor) ==0:
            print("Este campo no puede estar vacio")
        else:
            if len(valor)<3 or len(valor) >20:
                print("Lo solicitado debe tener entre 3 y 20 caracteres")
            else:
                return valor
            
def vHora(hora):
    while True: 
        fechastr= input("Hora de solicitud en formato (HH:MM) : ")
        try:
            hora=datetime.datetime.strptime(fechastr, "%H:%M")
            return hora
        except ValueError:
            print("Hora invalida")
    
def vFecha(fecha):
    while True:
        fechastr = input("Fecha de solicitud en formato (aaaa/mm/dd): ")
        try:
            fecha=datetime.datetime.strptime(fechastr, "%Y/%m/%d").date
            return fecha
        except ValueError:
            print("Fecha invalida")
        

def vehiculoExiste(conn, numSerie):
    cursor = conn.conexion.cursor()
    cursor.execute("SELECT COUNT(*) FROM vehiculo WHERE numSerie = %s", (numSerie,))
    return cursor.fetchone()[0] > 0


def vVehiculo(conn, msg):
    while True:
        v = input(msg)
        if len(v) == 17:  
            if vehiculoExiste(conn, v):
                return v
            else:
                print("Ese vehículo NO existe en la BD.")
        else:
            print("El número de serie debe tener 17 caracteres.")



def estadoExiste(conn, idEstado):
    cursor = conn.conexion.cursor()
    cursor.execute("SELECT COUNT(*) FROM edo_solicitud WHERE numero = %s", (idEstado,))
    return cursor.fetchone()[0] > 0

def vEstado(conn, msg):
    while True:
        est = input(msg)
        if est.isdigit():
            if estadoExiste(conn, est):
                return est
            else:
                print("Ese estado NO existe.")
        else:
            print("Solo números.")

def empleadoExiste(conn, idEmpleado):
    cursor = conn.conexion.cursor()
    cursor.execute("SELECT COUNT(*) FROM empleado WHERE numero = %s", (idEmpleado,))
    return cursor.fetchone()[0] > 0

def vEmpleado(conn, msg):
    while True:
        emp = input(msg)
        if emp.isdigit():
            if empleadoExiste(conn, emp):
                return emp
            else:
                print("Ese empleado NO existe.")
        else:
            print("Solo números enteros.")
