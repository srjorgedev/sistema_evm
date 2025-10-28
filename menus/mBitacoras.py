from interfaz import caja as UI

opcBitacoras = [
    "Crear bitacora",
    "Listado de bitacoras",
    "Consultar bitacora",
    "Volver",
]

CrearBitacora = [
    "Registrar salida",
    "Registrar entrada",
    "Volver",
]

# 0.1
def _Bitacoras():
    UI._Titulo("BITACORAS")
    UI._BordeV()
    UI._Lista(opcBitacoras)
    UI._BordeV()
    UI._LineaInf()

# 0.1.2
def _CrearBitacora():
    UI._Titulo("CREAR BITACORA")
    UI._BordeV()
    UI._Lista(CrearBitacora)
    UI._BordeV()
    UI._LineaInf()