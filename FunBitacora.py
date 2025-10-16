def _Listado():
    print("\n    LISTADO DE BITACORAS")
    print(f"\n    Num.Control {'─'*12} Asunto {'─'*12} Destino {'─'*12} Salida {'─'*12} Entrada \n")

    print("    00000124567              Comprar material    Soriana                 +                    -  ")
    print("    00000124567              Comprar material    Soriana                 +                    -  ")
    print("    00000124567              Comprar material    Soriana                 +                    -  ")
    print("    00000124567              Comprar material    Soriana                 +                    -  ")
    print("    00000124567              Comprar material    Soriana                 +                    -  ")
    print("    00000124567              Comprar material    Soriana                 +                    -  ")
    print("    00000124567              Comprar material    Soriana                 +                    -  ")
    print("    00000124567              Comprar material    Soriana                 +                    -  ")
    print("    00000124567              Comprar material    Soriana                 +                    -  ")

    input("\n    Presione ENTER para salir...")
    
def _Consulta():
    print("\n    Consultar bitacora\n")
    
    aux = input("    Numero de control de la bitacora a consultar: ")
    print(f"\n    No existe una bitacora con el numero de control: {aux}")
    
    input("\n    Presione ENTER para continuar...")
    
def _Salida():
    print("    REGISTRAR SALIDA\n")
    asunto = input("    Asunto: ")
    destino = input("    Destino: ")
    usuario = input("    Empleado que sale: ")
    autorizador = input("    Autorizado por: ")
    fecha = input("    Fecha de salida: ")
    hora = input("    Hora de salida: ")
    kilometraje = input("    Kilometraje: ")
    gasolima = input("    Litros de gasolina: ")
    
    print(f"""
    Salida registrada.
    
    Asunto: {asunto}          
    Destino: {destino}
    Empleado que sale: {usuario}
    Autorizado por: {autorizador}
    Fecha y hora de salida: {fecha} - {hora}
    Kilometraje al salir: {kilometraje}
    Litros de gasolina al salir: {gasolima} 
    
    Volviendo al menu de crear bitacora...
""")
    
def _Entrada():
    print("    REGISTRAR ENTRADA\n")
    fecha = input("    Fecha de entrada: ")
    hora = input("    Hora de entrada: ")
    kilometraje = input("    Kilometraje: ")
    gasolima = input("    Litros de gasolina: ")
    
    print(f"""
    Entrada registrada.
    
    Fecha y hora de entrada: {fecha} - {hora}
    Kilometraje al entrar: {kilometraje}
    Litros de gasolina al entrar: {gasolima} 
    
    Volviendo al menu de crear bitacora...
""")
    
def _Generar():
    print("    GENERAR BITACORA\n")
    print("    No es posible generar una bitacora")