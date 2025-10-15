import Listas
# Vista de la empresa

# 0
def _Principal():
    print("SISTEMA DE GESTION DE ENTRADA, SALIDA Y MANTENIMIENTO DE VEHICULOS")
    for e in Listas._MenuPrincipal:
        print(f"{Listas._MenuPrincipal.index(e) + 1}. {e}")

# 0.1
def _Bitacoras():
    print("\n    BITACORAS\n")
    print("    1. Listado de bitacoras")
    print("    2. Crear bitacora")
    print("    3. Editar bitacora")
    print("    4. Consultar bitacora")
    print("    5. Volver")

# 0.1.2
def _CrearBitacora():
    print("\n    CREAR BITACORA\n")
    print("    1. Registrar salida")
    print("    2. Registrar entrada")
    print("    3. Generar bitacora")
    print("    4. Volver")

# 0.2
def _Vehiculos():
    print("- VEHICULOS -")
    print("  1. Listado de vehiculos")
    print("  2. Agregar vehiculo")
    print("  3. Modificar informacion de vehiculo")
    print("  4. Eliminar vehiculo")
    print("  5. Suspender vehiculo")
    print("  6. Volver")

# 0.3
def _Mantenimiento():
    print("- MANTENIMIENTO -")
    print("  1. Listado de mantenimientos")
    print("  2. Solicitar mantenimiento")
    print("   ...")
    print("  6. Volver")

# 0.4
def _Observaciones():
    print("- OBSERVACIONES -")
    print("  1. Listado de observaciones")
    print("   ...")
    print("  6. Volver")

# 0.5
def _Solicitudes():
    print("- SOLICITUDES -")
    print("  1. Listado de solicitudes")
    print("  2. Levantar solicitud")
    print("  6. Volver")

# 0.6
def _Usuarios():
    print("- CHOFERES -")
    print("  1. Listado de usuarios")
    print("  2. Registrar usuario")
    print("  6. Volver")

# 0.7
def _Autorizar():
    print("- AUTORIZAR SOLICITUDES -")
    print("  1. Listado de solicitudes")
    print("  2. Listado de autorizaciones")
    print("  6. Volver")