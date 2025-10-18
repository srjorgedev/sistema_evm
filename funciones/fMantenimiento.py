mantenimientos = []


def _Listado():
    print("\n--- Listado de mantenimientos ---")
    if len(mantenimientos) == 0:
        print("No hay mantenimientos registrados.")
    else:
        for i, m in enumerate(mantenimientos, 1):
            print(
                f"{i}. Vehiculo: {m['vehiculo']} | Tipo: {m['tipo']} | Fecha: {m['fecha']} | Observaciones: {m['observaciones']}"
            )


def _Agregar():
    print("\n--- Solicitar mantenimiento ---")
    vehiculo = input("Ingrese el nombre o ID del vehiculo: ")
    tipo = input("Ingrese el tipo de mantenimiento (preventivo/correctivo): ")
    fecha = input("Ingrese la fecha del mantenimiento (DD/MM/AAAA): ")
    observ = input("Ingrese observaciones generales")
    mantenimiento = {
        "vehiculo": vehiculo,
        "tipo": tipo,
        "fecha": fecha,
        "observaciones": observ
    }
    mantenimientos.append(mantenimiento)
    print("Mantenimiento registrado correctamente.")
