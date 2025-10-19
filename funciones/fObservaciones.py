from . import fMantenimiento as m 

observaciones = []


def _Listado():
    print("\n--- Listado de observaciones ---")
    if len(observaciones) == 0:
        print("No hay observaciones registradas.")
    else:
        for i, obs in enumerate(observaciones, 1):
            print(
                f"{i}. Vehiculo: {obs['vehiculo']} | Tipo: {obs['tipo']} | Descripcion: {obs['descripcion']} | Fecha: {obs['fecha']}"
            )


def _Agregar():
    print("\n--- Registrar observacion ---")
    vehiculo = input("Ingrese el nombre o ID del vehiculo: ")
    tipo = input("Tipo de incidente/observacion (leve, media, grave): ")
    descripcion = input("Descripcion detallada del incidente: ")
    fecha = input("Ingrese la fecha (DD/MM/AAAA)")
    obs = {
        "vehiculo": vehiculo,
        "tipo": tipo,
        "descripcion": descripcion,
        "fecha": fecha,
    }
    observaciones.append(obs)
    print("Observacion registrada correctament")
    respuesta = (
        input("¿Desea registrar un mantenimiento relacionado? (S/N): ").strip().upper()
    )
    if respuesta == "S":
        print("\nRedirigiendo al registro de mantenimiento...\n")
        vehiculo_m = vehiculo
        tipo_m = input("Ingrese el tipo de mantenimiento (preventivo/correctivo): ")
        fecha_m = input("Ingrese la fecha del mantenimiento (DD/MM/AAAA): ")
        observ_m = input("Ingrese observaciones generales")
        mantenimiento = {
            "vehiculo": vehiculo_m,
            "tipo": tipo_m,
            "fecha": fecha_m,
            "observaciones": observ_m,
        }
        m.mantenimientos.append(mantenimiento)
        print("Mantenimiento registrado correctamente.")
    else:
        print("No se registró mantenimiento adicional.")
