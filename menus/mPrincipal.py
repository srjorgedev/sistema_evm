from interfaz import caja as UI

opciones: list[str] = [
    "Bitacoras", "Vehiculos", "Autorizar", "Solicitudes", "Usuarios",
    "Mantenimiento", "Observaciones", "Salir"
]

# 0
def _Principal():
    UI._Titulo(
        "SISTEMA DE GESTION DE ENTRADA, SALIDA Y MANTENIMIENTO DE VEHICULOS")
    UI._Lista(opciones)

