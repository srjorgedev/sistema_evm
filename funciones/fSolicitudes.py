def _Listado():
    print("Listado de solicitudes")
    print("solicitudes de vehiculos:")
    print("En construccion...")
    print("Solicitudes de mantenimiento:")
    print("En construccion...")


def _Levantar():
    print("Levantar solicitud")
    print("Tipo de solicitud (Mantenimiento/vehiculo): ")
    tipo_solicitud = input()
    print("Motivo de la solicitud: ")
    motivo_solicitud = input()
    print("Fecha de solicitud (dd/mm/aaaa): ")
    fecha_solicitud = input()
    print("Hora de solicitud (hh:mm): ")
    hora_solicitud = input()
    print("Nombre del solicitante: ")
    nombreSoli = input()
    print("Apellido paterno del solicitante: ")
    apellidopSoli = input()
    print("Apellido materno del solicitante: ")
    apellidomSoli = input()
    print("Numero de empleado del solicitante: ")
    num_empleado = input()
    print("Tipo de licencia del solicitante: ")
    tipo_licencia_soli = input()
    print("Fecha de vencimiento de la licencia (dd/mm/aaaa): ")
    fecha_vencimiento = input()
    print("Telefono del solicitante: ")
    telefono = input()
    print("Generar solicitud (1), modificar solicitud (2), cancelar (3): ")
    solicitud = input()
    if solicitud == "1":
        print("La solicitud ha sido generada exitosamente.")
    elif solicitud == "2":
        print("Modificar solicitud")
    else:
        print("Cancelando...")


def _Modificar():
    print("Modificar solicitud")
    print("Que solicitud desea modificar?")
    solicitudMod = input()
    print("Que dato desea modificar?")
    datoMod = input()
    print("Motivo de la modificacion: ")
    motivoMod = input()
    print("Por favor ingrese el nuevo valor:")
    nuevoValor = input()
    print(
        f"El dato {datoMod} de la solicitud {solicitudMod} ha sido modificado a {nuevoValor} por la siguiente razon: {motivoMod}."
    )


def _ConsultarEstado():
    print("Ver estado de la solicitud")
    print("Que solicitud desea consultar?")
    solicitudCon = input()
    print(f"El estado actual de la solicitud {solicitudCon} es: En proceso.")


def _Eliminar():
    print("Eliminar solicitud")
    print("Que solicitud desea eliminar?")
    solicitudEli = input()
    print("Cual es la razon de eliminar la solicitud?")
    razonEli = input()
    print(
        f"La solicitud {solicitudEli} ha sido eliminada por la siguiente razon: {razonEli}."
    )
