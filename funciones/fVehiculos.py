def _Listado():
    print("Listado de vehiculos")
    print("los vehiculos registrados son:")
    print("En construccion...")


def _Agregar():
    print("Agregar vehiculo")
    print("Ingresa el numero de serie del vehiculo: ")
    num_serie = input()
    print("Ingresa la matricula del vehiculo: ")
    matricula = input()
    print("Ingresa la marca del vehiculo: ")
    marca = input()
    print("Ingresa el modelo del vehiculo: ")
    modelo = input()
    print("Ingresa el color del vehiculo: ")
    color = input()
    print("Ingresa la fecha de fabricacion del vehiculo (dd/mm/aaaa): ")
    fecha_fabricacion = input()
    print("Ingresa la fecha de adquision del vehiculo (dd/mm/aaaa): ")
    fecha_adquision = input()
    print("Ingresa el tipo de vehiculo: ")
    tipo = input()
    print("Tipo de licencia requerida: ")
    tipo_licencia = input()
    print("Capacidad de pasajeros: ")
    capacidad_pasajeros = input()
    print("Utilidad del vehiculo: ")
    utilidad = input()
    print("comentarios adicionales: ")
    comentarios = input()
    print("El vehiculo ha sido registrado exitosamente.")


def _Modificar():
    print("Modificar informacion de vehiculo")
    print("Que vehiculo desea modificar?")
    vehiculoMod = input()
    print("Que dato desea modificar?")
    datoMod = input()
    print("Por favor ingrese el nuevo valor:")
    nuevoValor = input()
    print(
        f"El dato {datoMod} del vehiculo {vehiculoMod} ha sido modificado a {nuevoValor}."
    )


def _Eliminar():
    print("Eliminar vehiculo")
    print("Que vehiculo desea eliminar?")
    vehiculoEli = input()
    print("Cual es la razon de eliminar el vehiculo?")
    razonEli = input()
    print(
        f"El vehiculo {vehiculoEli} ha sido eliminado por la siguiente razon: {razonEli}."
    )


def _Suspender():
    print("Suspender vehiculo")
    print("Que vehiculo desea suspender?")
    vehiculoSus = input()
    print("Cual es la razon de suspender el vehiculo?")
    razonSus = input()
    print("Fecha de inicio de suspension (dd/mm/aaaa): ")
    fechaInicio = input()
    print("fecha de fin de suspension (dd/mm/aaaa): ")
    fechaFin = input()
    print(
        f"El vehiculo {vehiculoSus} ha sido suspendido por la siguiente razon: {razonSus}."
    )
    print(f"La suspension sera efectiva desde {fechaInicio} hasta {fechaFin}.")
