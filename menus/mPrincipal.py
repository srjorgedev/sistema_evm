from interfaz import caja as UI

opciones: list[str] = [
    "Bitacoras", "Vehiculos", "Autorizar", "Solicitudes", "Usuarios",
    "Mantenimiento", "Observaciones", "Salir"
]

# 0
def _Principal():
    UI._Titulo(
        "SISTEMA DE GESTION DE ENTRADA, SALIDA Y MANTENIMIENTO DE VEHICULOS")
    print("    1. Bitacoras")
    print("    2. Vehiculos")
    print("    3. Autorizar")
    print("    4. Solicitudes")
    print("    5. Usuarios")
    print("    6. Mantenimiento")
    print("    7. Observaciones")
    print("    8. Salir\n")
